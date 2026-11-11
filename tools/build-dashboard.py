#!/usr/bin/env python3
"""Сборка дашборда вакансий: data/vacancies/*/ → data/vacancies/dashboard.html.

Статический дашборд: карточки всех вакансий, фильтры, статусы, прогресс
чеклиста, следующее действие и дедлайны follow-up. Только чтение данных –
скрипт ничего не меняет в папках вакансий.

Использование:
    python3 tools/build-dashboard.py            # → data/vacancies/dashboard.html

Источники на каждую папку data/vacancies/<slug>/:
- <slug>-checklist-state.json – живой статус, галочки и даты чеклиста;
- content.json                – компания, роль, режим, match, вердикт, JD;
- data/vacancies/INDEX.md          – трекер (статус, роль, вердикт, фоллбэк);
- data/INDEX.md (корень)       – доп. фоллбэк статуса/вердикта;
- наличие index.html          – ссылка «Отчёт».

Приоритет статуса: checklist-state.json → data/vacancies/INDEX.md → content.json
→ data/INDEX.md (корень) → new.  Прогресс: n/visible (для network режима
пункты «Отклик» и «Сохранить описание» скрыты – 8 из 10, как в отчёте).
Дедлайны follow-up – логика из prompts/status.md.
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAC_DIR = ROOT / "data" / "vacancies"
OUT_PATH = VAC_DIR / "dashboard.html"

STATUS_ORDER = [
    "new", "researching", "applied", "screening",
    "interview", "offer", "rejected", "closed",
]
TERMINAL_STATUSES = ("closed", "rejected")

VISIBLE = {
    "application": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "network": ["1", "4", "5", "6", "7", "8", "9", "10"],
}

# Названия пунктов чеклиста (из templates/report.html, ru-строки t1..t10).
# Network-режим: пункты 2/3 скрыты, нумерация сдвинута – как в отчёте.
TITLES = {
    "application": {
        "1": "1. Адаптация / создание резюме",
        "2": "2. Отклик",
        "3": "3. Сохранить описание вакансии и название должности",
        "4": "4. Найти рекрутеров, нанимающих iOS-менеджеров и команду",
        "5": "5. Отправить рекрутеру персонализированный запрос в контакты",
        "6": "6. Написать нанимающему менеджеру короткое сообщение в LinkedIn",
        "7": "7. Лайкать и содержательно комментировать публикации HM после принятия запроса",
        "8": "8. Первый follow-up рекрутеру – через 5–7 рабочих дней после отклика",
        "9": "9. Финальное вежливое сообщение – на 10–14 день",
        "10": "10. После второго follow-up без ответа – переключиться на другие вакансии",
    },
    "network": {
        "1": "1. Адаптация / создание резюме",
        "4": "2. Найти рекрутеров, нанимающих iOS-менеджеров и команду",
        "5": "3. Отправить рекрутеру персонализированный запрос в контакты",
        "6": "4. Написать нанимающему менеджеру короткое сообщение в LinkedIn",
        "7": "5. Лайкать и содержательно комментировать публикации HM после принятия запроса",
        "8": "6. Первый follow-up рекрутеру – через 5–7 рабочих дней после первого сообщения",
        "9": "7. Финальное вежливое сообщение – на 10–14 день",
        "10": "8. После второго follow-up без ответа – переключиться на другие вакансии",
    },
}

NO_CHECKLIST_NEXT = {
    "new": "начать обработку",
    "researching": "продолжить обработку",
    "applied": "проверить чеклист",
}


# ---------- утилиты данных ----------

def strip_md(s: str) -> str:
    """Markdown/HTML → простой текст одной строкой."""
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`#]+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def one_liner(s: str, limit: int = 160) -> str:
    """Первое предложение (или начало текста) до ~limit символов."""
    t = strip_md(s)
    if not t:
        return ""
    if len(t) <= limit:
        return t
    parts = re.split(r"(?<=[.!?…])\s+", t)
    acc = ""
    for p in parts:
        if acc and len(acc) + 1 + len(p) > limit:
            break
        acc = (acc + " " + p).strip() if acc else p
        if len(acc) >= limit:
            break
    if not acc:
        acc = parts[0]
    if len(acc) > limit:
        acc = acc[: limit - 1].rstrip() + "…"
    return acc


def add_working_days(d: datetime.date, n: int) -> datetime.date:
    """+n рабочих дней (пн–пт), как addWorkingDays в отчёте."""
    cur, added = d, 0
    while added < n:
        cur += datetime.timedelta(days=1)
        if cur.weekday() < 5:
            added += 1
    return cur


def working_days_after(start: datetime.date, end: datetime.date) -> int:
    """Рабочие дни строго после start, включая end (если он рабочий)."""
    if end <= start:
        return 0
    n, cur = 0, start
    while cur < end:
        cur += datetime.timedelta(days=1)
        if cur.weekday() < 5:
            n += 1
    return n


def parse_date(s):
    try:
        return datetime.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def compute_deadlines(mode, dates, checks, today):
    """Окна/просрочки follow-up – prompts/status.md + логика отчёта."""
    out = []
    anchor = parse_date((dates or {}).get("5" if mode == "network" else "2"))
    if not anchor:
        return out
    f1a = add_working_days(anchor, 5)
    f1b = add_working_days(anchor, 7)
    f2a = anchor + datetime.timedelta(days=10)
    f2b = anchor + datetime.timedelta(days=14)
    c8, c9 = bool((checks or {}).get("8")), bool((checks or {}).get("9"))
    if not c8:
        if today > f1b:
            out.append({"kind": "overdue", "text": "просрочен первый follow-up"})
        elif today >= f1a:
            out.append({"kind": "window", "text": f"окно follow-up до {f1b.isoformat()}"})
    if not c9:
        if today > f2b:
            out.append({"kind": "overdue", "text": "просрочено финальное сообщение"})
        elif today >= f2a:
            out.append({"kind": "window", "text": f"окно финального до {f2b.isoformat()}"})
    if c8 and not c9:
        d8 = parse_date((dates or {}).get("8"))
        if d8 and 1 <= working_days_after(d8, today) <= 2:
            out.append({"kind": "soon", "text": "пора финальное сообщение"})
    order = {"overdue": 0, "soon": 1, "window": 2}
    out.sort(key=lambda x: order[x["kind"]])
    return out


def parse_index_md(path: Path, folder_idx: int, status_idx: int, extra_idx=None):
    """Парс строк таблицы INDEX.md → {folder: {status, ...}}."""
    res = {}
    if not path.exists():
        return res
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) <= max(folder_idx, status_idx):
            continue
        if cells[0] == "Дата" or set(cells[0]) <= set("-: "):
            continue
        folder = cells[folder_idx].strip("`").rstrip("/")
        folder = folder.rsplit("/", 1)[-1]  # корневой INDEX: "data/vacancies/<slug>"
        if not folder or folder in ("–", "-"):
            continue
        entry = {"status": cells[status_idx]}
        if extra_idx is not None and len(cells) > extra_idx:
            entry["extra"] = cells[extra_idx]
        res[folder] = entry
    return res


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


# ---------- сборка данных ----------

def build_item(folder: Path, idx_vac, idx_root, today) -> dict:
    slug = folder.name
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-", slug)
    date = m.group(1) if m else ""

    cl_path = next(iter(sorted(folder.glob("*checklist-state.json"))), None)
    cl = load_json(cl_path) if cl_path else None
    content = load_json(folder / "content.json")
    content = content if isinstance(content, dict) else None
    vac = idx_vac.get(slug, {})
    root = idx_root.get(slug, {})

    # статус: живой чеклист → трекер vacancies → content → корневой INDEX → new
    status = (cl or {}).get("status") or vac.get("status") \
        or (content or {}).get("status") or root.get("status") or "new"
    if status not in STATUS_ORDER:
        status = "new"

    mode = (content or {}).get("mode")
    if mode not in ("application", "network"):
        cell = vac.get("extra") if isinstance(vac.get("extra"), str) else None
        mode = cell if cell in ("application", "network") else None
    if mode not in ("application", "network"):
        mode = "network" if slug.endswith("-network") else "application"

    company = (content or {}).get("company") or vac.get("company")
    if not company:
        company = slug
    company = re.sub(r"\s*\((?:application|network)\)\s*$", "", strip_md(company))

    role = (content or {}).get("role") or vac.get("role") or ""

    match_pct = (content or {}).get("match_pct")
    if isinstance(match_pct, str):
        mm = re.search(r"\d+", match_pct)
        match_pct = int(mm.group()) if mm else None
    if isinstance(match_pct, (int, float)):
        match_pct = int(match_pct)
    else:
        match_pct = None

    url = (content or {}).get("vacancy_url") or ""
    if not url:
        lm = re.search(r"\((https?://[^)]+)\)", vac.get("link") or "")
        url = lm.group(1) if lm else ""

    verdict_full = strip_md((content or {}).get("verdict") or vac.get("verdict")
                            or root.get("verdict") or "")

    has_report = (folder / "index.html").exists()

    # прогресс и следующее действие
    checks = (cl or {}).get("checks") or {}
    dates = (cl or {}).get("dates") or {}
    has_checklist = cl is not None
    visible = VISIBLE[mode]
    done = sum(1 for i in visible if checks.get(i))
    total = len(visible)
    next_action = None
    if has_checklist:
        if done < total:
            next_action = TITLES[mode].get(
                next(i for i in visible if not checks.get(i)))
    else:
        next_action = NO_CHECKLIST_NEXT.get(status)

    deadlines = compute_deadlines(mode, dates, checks, today) if has_checklist else []

    return {
        "slug": slug,
        "date": date,
        "company": company,
        "role": role,
        "mode": mode,
        "status": status,
        "match_pct": match_pct,
        "match_label": (content or {}).get("match_label") or "",
        "vacancy_url": url,
        "verdict_short": one_liner(verdict_full),
        "verdict_full": verdict_full,
        "has_report": has_report,
        "has_checklist": has_checklist,
        "done": done,
        "total": total,
        "next_action": next_action,
        "deadlines": deadlines,
    }


def build_items(today) -> list:
    idx_vac = parse_index_md(VAC_DIR / "INDEX.md", 7, 6, extra_idx=3)
    # доп. поля из data/vacancies/INDEX.md: роль(2), ссылка(4), вердикт(8)
    for line in (VAC_DIR / "INDEX.md").read_text(encoding="utf-8").splitlines() \
            if (VAC_DIR / "INDEX.md").exists() else []:
        if not line.startswith("|") or line.startswith("|---") or "Дата" in line.split("|")[1]:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 9:
            folder = cells[7].strip("`").rstrip("/")
            if folder in idx_vac:
                idx_vac[folder].setdefault("role", strip_md(cells[2]))
                idx_vac[folder].setdefault("link", cells[4])
                idx_vac[folder].setdefault("verdict", cells[8])
                idx_vac[folder].setdefault("company", strip_md(cells[1]))
    idx_root = parse_index_md(ROOT / "data" / "INDEX.md", 2, 3, extra_idx=4)
    for k, v in idx_root.items():
        if v.get("extra"):
            v["verdict"] = v.pop("extra")

    items = []
    for folder in sorted(VAC_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith("_") or folder.name.startswith("."):
            continue
        items.append(build_item(folder, idx_vac, idx_root, today))

    items.sort(key=lambda x: (x["date"], x["slug"]), reverse=True)
    return items


# ---------- HTML ----------

def render_html(items, today) -> str:
    data = json.dumps(items, ensure_ascii=False)
    data = data.replace("</", "<\\/")  # безопасно внутри <script>
    template = HTML_TEMPLATE.replace("__DASHBOARD_DATA__", data)
    return template.replace("__TODAY__", today.isoformat())


HTML_TEMPLATE = r"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Дашборд вакансий</title>
<style>
:root {
  --bg: #f4f5f7; --card: #ffffff; --border: #e3e5e9; --text: #1c2128;
  --muted: #6b7280; --accent: #2563eb; --ok: #16a34a; --warn: #d97706;
  --bad: #dc2626; --track: #e8eaee;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f1115; --card: #171a21; --border: #262b34; --text: #e6e8eb;
    --muted: #9aa1ac; --accent: #60a5fa; --ok: #4ade80; --warn: #fbbf24;
    --bad: #f87171; --track: #262b34;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; padding: 20px; background: var(--bg); color: var(--text);
  font: 14px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
header { display: flex; flex-wrap: wrap; align-items: baseline; gap: 12px; margin-bottom: 14px; }
h1 { font-size: 20px; margin: 0; }
.counters { color: var(--muted); font-size: 13px; }
.counters b { color: var(--text); font-variant-numeric: tabular-nums; }
.counters .hot b { color: var(--bad); }
.generated { margin-left: auto; color: var(--muted); font-size: 12px; }

.filters {
  display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center;
  background: var(--card); border: 1px solid var(--border); border-radius: 12px;
  padding: 12px 14px; margin-bottom: 16px; position: sticky; top: 0; z-index: 5;
}
.filters .group { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.filters .label { color: var(--muted); font-size: 12px; margin-right: 2px; }
#q {
  flex: 1 1 200px; min-width: 160px; padding: 7px 10px; border-radius: 8px;
  border: 1px solid var(--border); background: var(--bg); color: var(--text); font-size: 13px;
}
#q:focus { outline: 2px solid var(--accent); outline-offset: -1px; }
.chip {
  border: 1px solid var(--border); background: var(--bg); color: var(--text);
  border-radius: 999px; padding: 4px 11px; font-size: 12.5px; cursor: pointer;
}
.chip:hover { border-color: var(--accent); }
.chip.active { background: var(--accent); border-color: var(--accent); color: #fff; }
.chip .n { opacity: .65; font-variant-numeric: tabular-nums; }
.chip.active .n { opacity: .85; }
.toggle { display: flex; align-items: center; gap: 6px; font-size: 12.5px; color: var(--muted); cursor: pointer; }
select {
  padding: 6px 8px; border-radius: 8px; border: 1px solid var(--border);
  background: var(--bg); color: var(--text); font-size: 12.5px;
}

.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(315px, 1fr)); gap: 14px; }
.card {
  background: var(--card); border: 1px solid var(--border); border-radius: 12px;
  padding: 14px; display: flex; flex-direction: column; gap: 8px;
  transition: transform .12s ease, border-color .12s ease;
}
.card:hover { transform: translateY(-2px); border-color: var(--accent); }
.top { display: flex; align-items: center; gap: 7px; }
.company { font-weight: 650; font-size: 15px; flex: 1 1 auto; min-width: 0;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.role { color: var(--muted); font-size: 13px; min-height: 18px;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.badges { display: flex; flex-wrap: wrap; gap: 5px; }
.badge {
  font-size: 11.5px; padding: 2px 8px; border-radius: 999px; white-space: nowrap;
  border: 1px solid color-mix(in srgb, var(--c, var(--muted)) 40%, transparent);
  background: color-mix(in srgb, var(--c, var(--muted)) 14%, transparent);
  color: var(--c, var(--muted));
}
.st-new { --c: #8a8f98; } .st-researching { --c: #3b82f6; }
.st-applied { --c: #22c55e; } .st-screening { --c: #06b6d4; }
.st-interview { --c: #a855f7; } .st-offer { --c: #f59e0b; }
.st-rejected { --c: #ef4444; } .st-closed { --c: #64748b; }
.mode { --c: #8b5cf6; }
.match-ok { --c: var(--ok); } .match-warn { --c: var(--warn); } .match-bad { --c: var(--bad); }
.nodata { --c: var(--warn); }
.dl-overdue { --c: var(--bad); font-weight: 600; }
.dl-soon { --c: #ea580c; font-weight: 600; }
.dl-window { --c: var(--warn); }

.progress-row { display: flex; align-items: center; gap: 9px; }
.bar { flex: 1; height: 6px; background: var(--track); border-radius: 999px; overflow: hidden; }
.bar i { display: block; height: 100%; background: var(--accent); border-radius: 999px; }
.bar.full i { background: var(--ok); }
.pct { font-size: 12px; color: var(--muted); font-variant-numeric: tabular-nums; min-width: 44px; text-align: right; }
.next { font-size: 12.5px; color: var(--text); }
.next b { color: var(--accent); font-weight: 600; }
.next.done { color: var(--ok); }
.next.muted { color: var(--muted); }
.verdict {
  font-size: 12.5px; color: var(--muted); cursor: help;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.bottom {
  display: flex; align-items: center; gap: 12px; margin-top: auto;
  padding-top: 8px; border-top: 1px dashed var(--border);
  font-size: 12.5px; color: var(--muted);
}
.bottom a { color: var(--accent); text-decoration: none; }
.bottom a:hover { text-decoration: underline; }
.bottom .date { font-variant-numeric: tabular-nums; }
.bottom .spacer { flex: 1; }
.empty { grid-column: 1 / -1; text-align: center; color: var(--muted); padding: 40px 0; }
footer { margin-top: 18px; color: var(--muted); font-size: 12px; }
@media (max-width: 560px) { body { padding: 12px; } .generated { margin-left: 0; } }
</style>
</head>
<body>
<header>
  <h1>📊 Дашборд вакансий</h1>
  <div class="counters" id="counters"></div>
  <div class="generated">Собрано: __TODAY__</div>
</header>

<section class="filters">
  <input id="q" type="search" placeholder="Поиск: компания или роль" autocomplete="off">
  <div class="group" id="chips-status" data-group="status"><span class="label">Статус:</span></div>
  <div class="group" id="chips-mode" data-group="mode"><span class="label">Режим:</span></div>
  <div class="group" id="chips-match" data-group="match"><span class="label">Match:</span></div>
  <div class="group" id="chips-progress" data-group="progress"><span class="label">Прогресс:</span></div>
  <label class="toggle"><input type="checkbox" id="showDone"> показывать завершённые</label>
  <select id="sort" title="Сортировка">
    <option value="date_desc">Дата ↓</option>
    <option value="date_asc">Дата ↑</option>
    <option value="match">Match ↓</option>
    <option value="progress">Прогресс ↓</option>
    <option value="status">Статус</option>
  </select>
</section>

<main class="grid" id="grid"></main>

<footer>Источники: content.json · checklist-state.json · data/vacancies/INDEX.md · data/INDEX.md. Дашборд только читает данные – статусы меняются через HTML-отчёты и INDEX.</footer>

<script id="data" type="application/json">__DASHBOARD_DATA__</script>
<script>
"use strict";
const DATA = JSON.parse(document.getElementById("data").textContent);
const STATUS_ORDER = ["new","researching","applied","screening","interview","offer","rejected","closed"];
const state = { q: "", status: "all", mode: "all", match: "all", progress: "all",
                showDone: false, sort: "date_desc" };

const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g,
  (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const isFull = (i) => i.has_checklist && i.done >= i.total;
const isFinished = (i) => isFull(i) || i.status === "closed" || i.status === "rejected";
const hasOverdue = (i) => i.deadlines.some((d) => d.kind === "overdue");

function chip(group, val, label, count) {
  const active = state[group] === val ? " active" : "";
  const n = count == null ? "" : ' <span class="n">' + count + "</span>";
  return '<button class="chip' + active + '" data-group="' + group +
    '" data-val="' + val + '">' + label + n + "</button>";
}

function buildChips() {
  const present = new Set(DATA.map((i) => i.status));
  let h = chip("status", "all", "Все", DATA.length);
  for (const s of STATUS_ORDER) {
    if (!present.has(s)) continue;
    h += chip("status", s, s, DATA.filter((i) => i.status === s).length);
  }
  document.getElementById("chips-status").insertAdjacentHTML("beforeend", h);

  h = chip("mode", "all", "Все", null);
  for (const m of ["application", "network"]) {
    const n = DATA.filter((i) => i.mode === m).length;
    if (n) h += chip("mode", m, m, n);
  }
  document.getElementById("chips-mode").insertAdjacentHTML("beforeend", h);

  h = chip("match", "all", "Все", null)
    + chip("match", "ge75", "≥75", DATA.filter((i) => i.match_pct != null && i.match_pct >= 75).length)
    + chip("match", "mid", "45–74", DATA.filter((i) => i.match_pct != null && i.match_pct >= 45 && i.match_pct < 75).length)
    + chip("match", "lt45", "<45", DATA.filter((i) => i.match_pct != null && i.match_pct < 45).length);
  document.getElementById("chips-match").insertAdjacentHTML("beforeend", h);

  h = chip("progress", "all", "Все", null)
    + chip("progress", "nodata", "без данных", DATA.filter((i) => !i.has_checklist).length)
    + chip("progress", "partial", "в процессе", DATA.filter((i) => i.has_checklist && !isFull(i)).length)
    + chip("progress", "done", "завершённые", DATA.filter(isFull).length);
  document.getElementById("chips-progress").insertAdjacentHTML("beforeend", h);
}

function refreshChipActive() {
  document.querySelectorAll(".chip").forEach((el) => {
    el.classList.toggle("active", state[el.dataset.group] === el.dataset.val);
  });
}

function passes(i) {
  if (state.q && !(i.company + " " + i.role).toLowerCase().includes(state.q)) return false;
  if (state.status !== "all" && i.status !== state.status) return false;
  if (state.mode !== "all" && i.mode !== state.mode) return false;
  if (state.match !== "all") {
    if (i.match_pct == null) return false;
    if (state.match === "ge75" && i.match_pct < 75) return false;
    if (state.match === "mid" && (i.match_pct < 45 || i.match_pct >= 75)) return false;
    if (state.match === "lt45" && i.match_pct >= 45) return false;
  }
  const full = isFull(i);
  if (state.progress === "nodata" && i.has_checklist) return false;
  if (state.progress === "partial" && (!i.has_checklist || full)) return false;
  if (state.progress === "done" && !full) return false;
  if (state.progress === "all" && full && !state.showDone) return false;
  return true;
}

function sortItems(list) {
  const byDate = (a, b) => b.date.localeCompare(a.date) || b.slug.localeCompare(a.slug);
  const ratio = (i) => (i.has_checklist ? i.done / i.total : -1);
  switch (state.sort) {
    case "date_asc": return list.slice().sort((a, b) => a.date.localeCompare(b.date) || a.slug.localeCompare(b.slug));
    case "match": return list.slice().sort((a, b) => (b.match_pct ?? -1) - (a.match_pct ?? -1) || byDate(a, b));
    case "progress": return list.slice().sort((a, b) => ratio(b) - ratio(a) || byDate(a, b));
    case "status": return list.slice().sort((a, b) =>
      STATUS_ORDER.indexOf(a.status) - STATUS_ORDER.indexOf(b.status) || byDate(a, b));
    default: return list.slice().sort(byDate);
  }
}

function matchClass(p) { return p == null ? "" : p >= 75 ? "match-ok" : p >= 45 ? "match-warn" : "match-bad"; }

function card(i) {
  const badges = [];
  badges.push('<span class="badge mode">' + i.mode + "</span>");
  badges.push('<span class="badge st-' + i.status + '" title="статус">' + i.status + "</span>");
  if (i.match_pct != null)
    badges.push('<span class="badge ' + matchClass(i.match_pct) + '" title="' +
      esc(i.match_label) + '">Match ' + i.match_pct + "</span>");
  if (!i.has_checklist) badges.push('<span class="badge nodata">нет данных чеклиста</span>');
  for (const d of i.deadlines)
    badges.push('<span class="badge dl-' + d.kind + '">' + esc(d.text) + "</span>");

  let progress = "";
  if (i.has_checklist) {
    const pct = Math.round((i.done / i.total) * 100);
    progress = '<div class="progress-row"><span class="bar' +
      (isFull(i) ? " full" : "") + '"><i style="width:' + pct + '%"></i></span>' +
      '<span class="pct">' + i.done + " / " + i.total + "</span></div>";
  }

  let next;
  if (i.has_checklist && isFull(i)) {
    next = '<div class="next done">✓ чеклист пройден</div>';
  } else if (i.next_action) {
    next = '<div class="next"><b>→ след.:</b> ' + esc(i.next_action) + "</div>";
  } else {
    next = '<div class="next muted">→ –</div>';
  }

  const verdict = i.verdict_short
    ? '<div class="verdict" title="' + esc(i.verdict_full) + '">' + esc(i.verdict_short) + "</div>"
    : "";

  const links = [];
  if (i.has_report) links.push('<a href="' + encodeURIComponent(i.slug) + '/index.html">Отчёт ↗</a>');
  if (i.vacancy_url) links.push('<a href="' + esc(i.vacancy_url) + '" target="_blank" rel="noopener">Вакансия ↗</a>');

  return '<article class="card">' +
    '<div class="top"><span class="company" title="' + esc(i.company) + '">' + esc(i.company) + "</span></div>" +
    '<div class="role" title="' + esc(i.role) + '">' + esc(i.role || "–") + "</div>" +
    '<div class="badges">' + badges.join("") + "</div>" +
    progress + next + verdict +
    '<div class="bottom"><span class="date">' + (i.date || "–") + "</span>" +
    '<span class="spacer"></span>' + links.join(" · ") + "</div>" +
    "</article>";
}

function render() {
  const list = sortItems(DATA.filter(passes));
  const grid = document.getElementById("grid");
  grid.innerHTML = list.length
    ? list.map(card).join("")
    : '<div class="empty">Ничего не найдено – сбрось фильтры</div>';

  const active = list.filter((i) => !isFinished(i)).length;
  const finished = list.filter(isFinished).length;
  const overdue = list.filter(hasOverdue).length;
  document.getElementById("counters").innerHTML =
    "Показано <b>" + list.length + "</b> из " + DATA.length +
    " · Активных <b>" + active + "</b>" +
    " · Завершено <b>" + finished + "</b>" +
    ' · <span class="hot">Просрочено <b>' + overdue + "</b></span>";
}

document.getElementById("q").addEventListener("input", (e) => {
  state.q = e.target.value.trim().toLowerCase(); render();
});
document.querySelector(".filters").addEventListener("click", (e) => {
  const btn = e.target.closest(".chip");
  if (!btn) return;
  state[btn.dataset.group] = btn.dataset.val;
  refreshChipActive(); render();
});
document.getElementById("showDone").addEventListener("change", (e) => {
  state.showDone = e.target.checked; render();
});
document.getElementById("sort").addEventListener("change", (e) => {
  state.sort = e.target.value; render();
});

buildChips();
render();
</script>
</body>
</html>
"""


def main() -> int:
    today = datetime.date.today()
    items = build_items(today)
    if not items:
        print("Нет папок вакансий – ничего не собрано.", file=sys.stderr)
        return 1
    OUT_PATH.write_text(render_html(items, today), encoding="utf-8")

    by_status = {}
    for i in items:
        by_status[i["status"]] = by_status.get(i["status"], 0) + 1
    no_cl = sum(1 for i in items if not i["has_checklist"])
    overdue = sum(1 for i in items if any(d["kind"] == "overdue" for d in i["deadlines"]))
    print(f"Дашборд собран: {OUT_PATH.relative_to(ROOT)}")
    print(f"  вакансий: {len(items)}, без чеклиста: {no_cl}, просрочено: {overdue}")
    print("  статусы:", ", ".join(f"{k}={v}" for k, v in sorted(by_status.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
