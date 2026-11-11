#!/usr/bin/env python3
"""Сборка единого HTML вакансии из templates/report.html + content.json.

Агент НЕ читает шаблон и НЕ пишет HTML-файл целиком: кладёт данные в
data/vacancies/<slug>/content.json и запускает этот скрипт.

Использование:
    python3 tools/build-report.py data/vacancies/<slug>        # читает content.json → пишет index.html

Поля content.json (markdown допускается — таблицы/списки/абзацы конвертируются;
значение, начинающееся с '<', считается готовым HTML):
    company, role, lang (ru|en), mode (application|network),
    status (new|researching|applied|screening|interview|offer|rejected|closed),
    vacancy_url, match_pct, match_label,
    verdict, gap, gap_close, summary, achievements, cover_letter,
    company_research, people, draft_recruiter, draft_lead, draft_teammate
Необязательные: generated_at (default: сегодня), slug (default: имя папки).

`achievements` дополнительно может быть структурированным списком групп
«работодатель → проект → достижения» (структура повторяет CV; каждый проект
и каждое достижение получают свою copy-кнопку с контекстом проекта в буфере):
    [{"employer": "...", "role": "...", "period": "...",
      "projects": [{"project": "...", "period": "...", "items": ["..."]}]}]

Дополнительно:
- если в папке вакансии есть `cv-updated.md` (полное CV с закрытыми гэпами),
  в HTML добавляется ссылка на него (модуль «Обновлённое CV»); без файла модуль удаляется;
- ячейки таблиц со статусами (✅/⚠️/❌ или full/partial/gap) автоматически
  подсвечиваются зелёным/жёлтым/красным и получают эмодзи;
- цвет бейджа Match % считается из match_pct: ok ≥75, warn 45–74, bad <45.
"""
import json
import re
import sys
import datetime
from pathlib import Path

TEXT_FIELDS = [
    "company", "role", "lang", "mode", "status", "vacancy_url",
    "match_pct", "match_label", "match_class", "generated_at", "slug",
]
HTML_FIELDS = {
    "verdict": "VERDICT_HTML", "gap": "GAP_HTML", "gap_close": "GAP_CLOSE_HTML",
    "summary": "SUMMARY_HTML", "achievements": "ACHIEVEMENTS_HTML",
    "cover_letter": "COVER_LETTER_HTML", "company_research": "COMPANY_HTML",
    "people": "PEOPLE_HTML", "draft_recruiter": "DRAFT_RECRUITER_HTML",
    "draft_lead": "DRAFT_LEAD_HTML", "draft_teammate": "DRAFT_TEAMMATE_HTML",
}

RE_HEADING = re.compile(r"^(#{2,4})\s+(.*)")
RE_NUM = re.compile(r"^\d+\.\s")
RE_TABLE_ROW = re.compile(r"^\|")
RE_MD_START = re.compile(r"^(#{2,4}\s|[-*]\s|\d+\.\s|\||```)")
RE_URL = re.compile(r"https?://[^\s<\"')\]]+")
RE_TAG_SPLIT = re.compile(r"(<[^>]*>)")
RE_NESTED_A = re.compile(r'<a href="(https?://[^\"]+)"><a href="[^\"]+">\1</a></a>')


def md_inline(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    # кликабельные ссылки: bare URL в тексте (не внутри тегов)
    parts = RE_TAG_SPLIT.split(s)
    for i in range(0, len(parts), 2):
        parts[i] = RE_URL.sub(lambda m: '<a href="%s">%s</a>' % (m.group(0), m.group(0)), parts[i])
    s = "".join(parts)
    s = RE_NESTED_A.sub(r'<a href="\1">\1</a>', s)
    return s


def md_block(text: str) -> str:
    """Консервативный markdown → HTML: заголовки, списки, таблицы, абзацы."""
    out, lines, i = [], text.strip().splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# ") and not line.startswith("## "):
            # H1 из исходного .md дублирует заголовок модуля – не выводим
            i += 1
            continue
        m = RE_HEADING.match(line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if line.lstrip().startswith("```"):
            # fenced code (```json, ```bash, ...) – выводим как есть, без разметки и ссылок
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = (("\n".join(buf)).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            out.append('<pre class="code"><code>' + code + "</code></pre>")
            continue
        if line.lstrip().startswith(("- ", "* ")):
            items = []
            while i < len(lines) and lines[i].lstrip().startswith(("- ", "* ")):
                items.append("<li>" + md_inline(lines[i].lstrip()[2:]) + "</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        if RE_NUM.match(line.lstrip()):
            items = []
            while i < len(lines) and RE_NUM.match(lines[i].lstrip()):
                text_item = RE_NUM.sub("", lines[i].lstrip())
                items.append("<li>" + md_inline(text_item) + "</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        if RE_TABLE_ROW.match(line.strip()):
            rows = []
            while i < len(lines) and RE_TABLE_ROW.match(lines[i].strip()):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.fullmatch(r"[-: ]+", "".join(cells)):
                    rows.append(cells)
                i += 1
            if rows:
                head = "".join("<th>" + md_inline(c) + "</th>" for c in rows[0])
                body = ""
                for r in rows[1:]:
                    body += "<tr>" + "".join(status_cell(c) for c in r) + "</tr>"
                out.append("<table><thead><tr>" + head + "</tr></thead><tbody>" + body + "</tbody></table>")
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not RE_MD_START.match(lines[i].lstrip()):
            para.append(lines[i])
            i += 1
        out.append("<p>" + "<br>".join(md_inline(p) for p in para) + "</p>")
    return "\n".join(out)


def match_tone(pct) -> str:
    """ok | warn | bad для значения Match %: ok ≥75, warn 45–74, bad <45."""
    try:
        p = float(str(pct).replace("%", "").strip())
    except (TypeError, ValueError):
        return "warn"
    return "ok" if p >= 75 else ("warn" if p >= 45 else "bad")


STATUS_EMOJI = {"st-ok": "✅", "st-warn": "⚠️", "st-bad": "❌"}
RE_STATUS_OK = re.compile(r"^\s*(✅|🟢|full\b)", re.I)
RE_STATUS_WARN = re.compile(r"^\s*(⚠️|⚠|🟡|partial\b)", re.I)
RE_STATUS_BAD = re.compile(r"^\s*(❌|🔴|gap\b)", re.I)


def status_class(raw: str):
    """Класс подсветки ячейки таблицы со статусом (или None)."""
    if RE_STATUS_OK.match(raw):
        return "st-ok"
    if RE_STATUS_WARN.match(raw):
        return "st-warn"
    if RE_STATUS_BAD.match(raw):
        return "st-bad"
    return None


def status_cell(raw: str) -> str:
    """<td> с подсветкой и эмодзи статуса (эмодзи добавляется, если его нет)."""
    inner = md_inline(raw)
    cls = status_class(raw)
    if cls is None:
        return "<td>" + inner + "</td>"
    if not re.match(r"^\s*(✅|⚠️|⚠|🟡|❌|🟢|🔴)", raw):
        inner = STATUS_EMOJI[cls] + " " + inner
    return '<td class="%s">%s</td>' % (cls, inner)


def _attr(s: str) -> str:
    return str(s).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def achievements_html(groups) -> str:
    """Сгруппированные достижения: работодатель → проект → bullets.

    Одна copy-кнопка на проект: копирует только текст булетов, без заголовка
    проекта и без служебного контекста.
    """
    css = (
        "<style>"
        ".ach-emp{margin-top:18px}"
        ".ach-emp>h3{margin:6px 0 8px}"
        ".ach-proj{border:1px solid var(--border);border-radius:10px;padding:10px 12px;margin:10px 0;background:var(--card2)}"
        ".ach-proj-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap}"
        ".ach-proj-head h4{margin:0;flex:1;min-width:220px}"
        ".ach-period{color:var(--muted);font-weight:400}"
        ".ach-item{margin:8px 0}"
        ".ach-item-text{flex:1}"
        "</style>"
    )
    out = [css]
    n = 0
    for g in groups:
        emp = str(g.get("employer", "")).strip()
        role = str(g.get("role", "")).strip()
        period = str(g.get("period", "")).strip()
        head = md_inline(emp)
        if role:
            head += " – " + md_inline(role)
        if period:
            head += ' <span class="ach-period">(%s)</span>' % md_inline(period)
        out.append('<div class="ach-emp"><h3>%s</h3>' % head)
        for p in g.get("projects", []):
            n += 1
            pid = "ach-%d" % n
            proj = str(p.get("project", "")).strip()
            pperiod = str(p.get("period", "")).strip()
            phead = md_inline(proj or emp)
            if pperiod:
                phead += ' <span class="ach-period">(%s)</span>' % md_inline(pperiod)
            out.append('<div class="ach-proj">')
            out.append(
                '<div class="ach-proj-head"><h4>%s</h4>'
                '<button class="copy-btn" data-copy="%s" data-i18n="copy">Copy</button></div>'
                % (phead, pid)
            )
            out.append('<div id="%s">' % pid)
            for j, item in enumerate(p.get("items", []), 1):
                iid = "%s-%d" % (pid, j)
                out.append(
                    '<div class="ach-item">'
                    '<div class="ach-item-text" id="%s">%s</div>'
                    "</div>"
                    % (iid, md_inline(str(item)))
                )
            out.append("</div></div>")
        out.append("</div>")
    return "\n".join(out)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    vac = Path(sys.argv[1])
    data = json.loads((vac / "content.json").read_text(encoding="utf-8"))

    data.setdefault("generated_at", datetime.date.today().isoformat())
    data.setdefault("slug", vac.name)
    # UI отчёта всегда русский: {{LANG}} берётся из content.json, но если его нет или он
    # вне ru|en – принудительно ru (контент-блоки от этого не меняются).
    data.setdefault("lang", "ru")
    if str(data.get("lang", "")).lower() not in ("ru", "en"):
        data["lang"] = "ru"
    # match_pct может прийти как 90, "90" или "84%" – «%» в шаблоне добавляется сам
    pct = str(data.get("match_pct", "")).strip().rstrip("%").strip()
    data["match_pct"] = pct
    data.setdefault("match_class", match_tone(pct))

    tpl = Path(__file__).resolve().parent.parent / "templates" / "report.html"
    html = tpl.read_text(encoding="utf-8")

    missing = []
    for field in TEXT_FIELDS:
        ph = "{{" + field.upper() + "}}"
        if ph not in html:
            continue
        if field not in data:
            missing.append(field)
            continue
        html = html.replace(ph, str(data[field]))

    for field, ph_name in HTML_FIELDS.items():
        ph = "{{" + ph_name + "}}"
        if ph not in html:
            continue
        if field not in data:
            missing.append(field)
            continue
        raw = data[field]
        if field == "achievements" and isinstance(raw, list):
            block = achievements_html(raw)
        else:
            value = str(raw)
            block = value if value.lstrip().startswith("<") else md_block(value)
        html = html.replace(ph, block)

    # ссылка на обновлённое CV (cv-updated.md); нет файла – модуль удаляем целиком
    if "{{CV_UPDATED_HTML}}" in html:
        if (vac / "cv-updated.md").exists():
            html = html.replace(
                "{{CV_UPDATED_HTML}}",
                '<a class="btn" href="cv-updated.md" target="_blank">cv-updated.md ↗</a>',
            )
        else:
            html = re.sub(
                r"[ \t]*<!-- cv-updated -->.*?<!-- /cv-updated -->\n?",
                "",
                html,
                flags=re.S,
            )

    leftovers = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if leftovers:
        missing.extend(sorted(set(leftovers)))

    out = vac / "index.html"
    out.write_text(html, encoding="utf-8")
    if missing:
        print("пустые поля:", ", ".join(sorted(set(missing))))
    print("OK " + str(out))


if __name__ == "__main__":
    main()
