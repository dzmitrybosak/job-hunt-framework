---
name: job-status
description: Job Hunt — статус по вакансиям списком/текстом в чат: прогресс чеклиста и следующее действие. Команда /job-status (или «status» текстом).
user-invocable: true
---

# job-status — статус Job Hunt

Выкинь статус в чат текстом/списком:

1. Найди в воркспейсе фреймворк (`job-hunt/` или `job-hunt-framework/`), прочитай `prompts/status.md` — основная процедура.
2. Собери данные: `data/vacancies/INDEX.md`, `data/vacancies/<slug>/checklist-state.json` (и `~/Downloads/*checklist-state.json`), посчитай прогресс n/10, следующее действие и просрочки follow-up.
3. Выведи в чат списком/таблицей текстом, по срочности; готовые 10/10 и вакансии со статусом `closed`/`rejected` (завершены автоматически) не показывать. Ничего не генерировать и в браузер не открывать.

Команда `/job-status`, потому что `/status` занят встроенной командой OpenClaw (статус сессии). Написанное текстом «status» — тоже эта команда.
