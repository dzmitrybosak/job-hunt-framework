---
name: company-flow
description: Job Hunt — работа по сайту компании: на входе ссылка, на выходе список вакансий или готовый HTML network-пакета, открытый в браузере. Команда /company-flow <ссылка>.
user-invocable: true
---

# company-flow — флоу 2 Job Hunt

Работа по ссылке на сайт компании из аргументов команды (если нет — спроси одну ссылку):

1. Найди в воркспейсе фреймворк (`job-hunt/` или `job-hunt-framework/`), прочитай `prompts/_common.md` и `prompts/company-intake.md`.
2. Карьерная страница → все открытые позиции → фильтр по `data/profile/target-role.md` → таблица в чат.
3. Есть подходящие → предложи `/vacancy-flow` для выбранных. Нет → network-пакет по процедуре + единый HTML (`content.json` + `python3 tools/build-report.py data/vacancies/<slug>`), открой `index.html` в браузере.
4. В чат — краткий итог (список вакансий или Match % + путь к файлу).

Сообщения и тексты — по процедурам `prompts/`; язык — по `prompts/output-language.md`.
