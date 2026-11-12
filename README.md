# Job Hunt Framework

Агент-фреймворк для поиска работы: master CV → поиск вакансий → анализ соответствия → research компании → люди из LinkedIn и Сетки → драфты сообщений → cover letter → единый HTML вакансии с чеклистом и кнопками Copy.

Работает с любым ИИ (Claude, ChatGPT, Codex, Cursor, OpenClaw...): подключается как проект, ИИ следует процедурам из `prompts/` и инструкциям из `AGENTS.md`.

## Что внутри

```
├── README.md            ← ты здесь
├── AGENTS.md            ← инструкции для ИИ (читается автоматически при подключении проекта)
├── PROJECT-INSTRUCTIONS.md ← готовый блок для Project instructions (Claude Projects / ChatGPT)
├── LICENSE              ← MIT
├── prompts/             ← промпты и процедуры (18 шт.)
│   ├── _common.md             сквозные правила и подстановки (paste → файлы)
│   ├── init.md                команда init-job-hunt: инициализация профиля кандидата
│   ├── self-interview.md      интервью → experience-insights (разово / при обновлении)
│   ├── vacancy-intake.md      флоу 1: вакансия → vacancy.md + гейт локации
│   ├── status.md              команда status: следующее действие по вакансиям
│   ├── gap-analysis.md        Match % + таблица требований
│   ├── gap-close.md           топ-3 пробела → готовые bullets / компенсация
│   ├── tailored-summary.md    summary: 3 строки, 75–80% keywords JD
│   ├── achievement-bullets.md bullets: verb + scope + result с цифрой + tool
│   ├── cover-letter.md        cover letter: 250 слов, 3 абзаца
│   ├── cold-message.md        cold message: 4 строки, observation → ask
│   ├── message-drafts.md      драфты: application / network
│   ├── find-vacancies.md      поиск вакансий по рынку (по запросу пользователя)
│   ├── company-intake.md      флоу 2: сайт компании → вакансии / network
│   ├── company-research.md    research компании
│   ├── find-people.md         люди из LinkedIn и Сетки + персонализация
│   ├── tailor-resume.md       сборка адаптированного резюме
│   └── output-language.md     язык вывода: EN/RU по вакансии/сайту, иначе — спросить
├── templates/
│   ├── report.html            единый HTML вакансии: чеклист + все блоки, Copy-кнопки, автосохранение состояния (UI всегда русский, контент-блоки – на языке вакансии)
│   └── vacancy/               шаблон папки на каждую вакансию: vacancy, company, gap-analysis, gap-close, resume-adapted, people, drafts/, cover-letter
├── tools/
│   ├── build-report.py        сборка index.html из content.json (экономит токены: агент не пишет HTML руками)
│   └── build-dashboard.py     сборка data/vacancies/dashboard.html – дашборд по всем вакансиям
├── .opencode/commands/      ← слэш-команды OpenCode: /init-job-hunt /vacancy-flow /company-flow /job-status /dashboard (читают skills/)
├── skills/                  ← слэш-команды /init-job-hunt /vacancy-flow /company-flow /job-status:
│                              для OpenClaw (авто) и для OpenCode (через .opencode/commands/)
└── data/                    ← ЛИЧНЫЕ ДАННЫЕ, в .gitignore — в git не попадает
    ├── profile/               твои данные (заполняешь один раз через /init-job-hunt)
    │   ├── master-cv.md       индекс: какую версию CV брать + общие факты
    │   ├── master-cv-ru.md    master CV на русском (для ru-вакансий)
    │   ├── master-cv-en.md    master CV на английском (для en-вакансий)
    │   ├── target-role.md     какую роль ищешь, keywords, условия + канон формулировки роли
    │   ├── positioning.md     позиционирование: метка и дескриптор, из которых собран канон роли
    │   ├── achievements.md    банк достижений с цифрами
    │   ├── links.md           LinkedIn, GitHub, контакты
    │   ├── self-interview.md  детальный опыт и истории (только чтение)
    │   └── experience-insights/ производный слой: index.md, topics/weak-notes.md, stories/{cv-bullets,star-stories}.md, evidence/evidence-map.md, gaps/bridges.md
    ├── vacancies/
    │   ├── INDEX.md           трекер вакансий
    │   ├── dashboard.html     дашборд всех вакансий (генерируется build-dashboard.py)
    │   └── <slug>/            пакет вакансии: vacancy, company, gap-analysis, gap-close, resume-adapted, people, drafts/, cover-letter + content.json, index.html, checklist-state.json
    └── reports/               разовые отчёты (пакет вакансии сюда не писать – он в vacancies/<slug>/)
```

## Быстрый старт

1. **Распакуй фреймворк** — двумя способами:
   - **в корень воркспейса ИИ** (его `skills/` = `<workspace>/skills/`) — OpenClaw и OpenCode регистрируют команды автоматически, нулевая настройка;
   - **в любую папку** — подключить как проект: команды работают обычным текстом по `AGENTS.md`. В OpenCode слэш-команды работают сразу (`.opencode/commands/` читают `skills/`); для OpenClaw слэш-команды появятся, если скопировать `skills/` в воркспейс.
2. **Заполни `data/profile/`** — просто набери `/init-job-hunt`: агент сам спросит недостающие блоки (master CV, желаемые роли 1–3, ссылки, условия, достижения); CV можно прислать сразу — файлом, текстом или ссылкой.
3. **Работай командами** – полный список с описаниями ниже, в разделе «Команды».
4. В других ИИ (Claude Projects, ChatGPT) те же команды работают обычным текстом: «init-job-hunt», «vacancy-flow» + текст JD и компания – настройка не нужна, `AGENTS.md` всё объясняет.

## Команды

Все команды работают и как слэш-команды (`/vacancy-flow`), и обычным текстом без слэша («vacancy-flow» + текст JD). Слэш-вариант доступен там, где среда подхватила `skills/` или `.opencode/commands/`.

| Команда | Вход | Что делает | Что на выходе |
|---|---|---|---|
| `/init-job-hunt` | ничего, дальше диалог | Интервью по пустым блокам профиля: master CV (RU + EN), желаемые роли 1–3 и must-have, формат и условия, ссылки, достижения. Если есть `self-interview.md` – обновляет производный слой `experience-insights/`. Заполненное не переспрашивает, инициатива на агенте. | Заполненный `data/profile/` + сводка в чат: что заполнено, чего не хватает |
| `/vacancy-flow` | ссылка на вакансию и/или текст JD + название компании | Флоу 1 целиком: intake → гейт локации/формата (не подходит – стоп) → research компании → Match % → топ-3 пробела с закрытием → адаптированное резюме (Summary + Key achievements 5–7 на проект + внепроектная деятельность) → люди из LinkedIn и Сетки → драфты сообщений → cover letter → сборка HTML последним шагом | `data/vacancies/<slug>/` со всем пакетом и `index.html`, открытым в браузере; в чат – Match %, 2–3 строки «что внутри» и путь к файлу |
| `/company-flow` | ссылка на сайт компании | Флоу 2: находит карьерную страницу и все открытые позиции, фильтрует по `target-role.md`. Есть подходящие – предлагает запустить `/vacancy-flow` по выбранным. Нет – собирает network-пакет (профильный Match %, open application, драфты про будущие вакансии/реферал). | Таблица вакансий в чат **или** network-пакет с `index.html` в браузере; строка в `data/vacancies/INDEX.md` |
| `/job-status` (или «status» текстом) | ничего | Считает по всем активным вакансиям прогресс чеклиста n/10, следующее действие и просрочки follow-up. Завершённые (10/10, `closed`, `rejected`) не показывает. Данные – `INDEX.md` + `checklist-state.json`. | Текст/таблица в чат по срочности; ничего не генерирует и браузер не открывает |
| `/dashboard` | ничего | Запускает `python3 tools/build-dashboard.py` – сборка дашборда из всех папок `data/vacancies/*/` (карточки, фильтры, статусы, прогресс чеклиста, следующее действие, дедлайны follow-up). Только читает данные. | `data/vacancies/dashboard.html`, открытый в браузере + короткий отчёт, сколько вакансий попало |

Отдельной команды нет, но есть процедуры по явной просьбе: **поиск вакансий по рынку** (`prompts/find-vacancies.md` – 3–5 запросов по твоей роли, таблица с вердиктами и строками в `INDEX.md`) и **self-interview** (`prompts/self-interview.md` – разовое превращение `data/profile/self-interview.md` в `experience-insights/`). Из флоу они сами не запускаются.

## Два флоу

**Флоу 1 — вакансия: ссылка или текст JD + компания.** На выходе: анализ компании · Match % твоего опыта · топ-3 пробела с закрытием · адаптированные Summary + Key achievements (5–7 релевантных булетов на проект) + внепроектная деятельность · люди из LinkedIn и Сетки (HM, рекрутеры, iOS-команда) · cold messages и teammate-драфты · cover letter · **единый HTML `data/vacancies/<slug>/index.html`**: компактные блоки всего вышеперечисленного + рабочий чеклист (отклик и follow-up по дням) с автосохранением галочек, статуса и дат.

**Флоу 2 — ссылка на сайт компании.** ИИ находит карьерную страницу и все открытые позиции, фильтрует по твоей роли. Есть подходящие → флоу 1 на каждую (можно и **текстом JD**, без ссылки). Нет → тот же пакет в network-режиме: профильный Match %, open application cover letter, драфты про будущие вакансии/реферал/чат.

## Подключение к ИИ

| Где | Как |
|---|---|
| Claude Code / Cursor / Codex | Открыть папку как проект — `AGENTS.md` подхватится автоматически. Слэш-команды: текстом (`vacancy-flow` и т.д.) или скопировать `skills/` в каталог скиллов своей среды |
| OpenCode | Открыть папку как проект: `AGENTS.md` + слэш-команды из `.opencode/commands/` (эти файлы читают `skills/`, поэтому папку удалять нельзя) |
| OpenClaw | Открыть папку как проект: `skills/` в корне воркспейса регистрирует слэш-команды автоматически |
| Claude Projects / ChatGPT Projects | **Обязательно:** вставь текст `PROJECT-INSTRUCTIONS.md` в Project instructions, файлы — в Project files. Без этого команды (`init-job-hunt` и т.д.) для модели — просто слова, они не сработают |
| Любой чат с загрузкой файлов | Приложи папку/zip + текст `PROJECT-INSTRUCTIONS.md` первым сообщением |

После подключения достаточно прислать ссылку на вакансию, **текст JD + название компании** или сайт компании.

## Кастомизация

- **Промпты** (`prompts/`) — редактируй под себя: тон, длина, запрещённые слова.
- **Отчёт и чеклист** (`templates/`) — обычный HTML/CSS/JS; Copy-кнопки и автосохранение уже работают, UI-подписи всегда русские, контент-блоки — на языке вакансии.
- **Язык** — тексты и контент-блоки на языке вакансии (ru/en), UI-подписи отчёта всегда на русском; если язык вакансии неясен, ИИ спросит тебя.

## Важно

- `data/` (профиль, вакансии, отчёты) в `.gitignore` — личные данные **не попадают в git**. Заполненный `data/profile/` не публикуй публично.
- Фреймворк устроен так, что ИИ **не выдумывает факты** о тебе: всё берётся из `data/profile/`, отсутствующее — спрашивается.

## Лицензия

MIT — используй, меняй, шарь.
