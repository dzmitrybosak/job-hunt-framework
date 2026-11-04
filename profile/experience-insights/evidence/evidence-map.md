# Evidence map: цифры и масштабы

Назначение: перед добавлением цифры в резюме, summary, cover letter или сообщение – проверить, где она подтверждена. `В<N>` – вопрос `profile/self-interview.md` (строки в `index.md`). Обновлено: 2026-11-04 (62 вопроса; добавлен блок AI-SDLC по В62).

## Цифры и масштабы из интервью

| Факт | Значение | Источник | Где уже подтверждено | Статус |
|---|---|---|---|---|
| Открытия через виджет | более 1 000 000 успешных открытий | В5, 89 | `achievements.md` A1; `master-cv-ru.md` | подтверждено |
| Проектирование Mock API | около 1 месяца | В4, 63 | нет в CV | только интервью |
| Проекты в Orangesoft | 5+ проектов | В2, 16 | CV перечисляет избранные проекты | частично |
| iOS-инженеры на проекте NDA1 | около 20–30 iOS-инженеров суммарно на проекте | В2, 27 + уточнение пользователя 2026-10-30 | нет в CV | подтверждено пользователем |
| Демо для заказчика | аудитория 100+ человек | В2, 29 | нет в CV | только интервью |
| iOS-команда на NDA2 | 4 инженера (CV; в интервью было 2–3 – ошибка) | В3, 43 + `master-cv-ru.md` | CV: 4 iOS-инженера | решено 2026-10-30 – использовать 4 |
| iOS-команда на NDA1 | 3–4 инженера в одной из команд | уточнение пользователя 2026-10-30 | CV: 4 iOS-инженера | согласуется с CV |
| Код-ревью | 15 минут – 1 час в день | В3, 43 | нет в CV | только интервью |
| Команды на проекте NDA1 | 5–7 отдельных команд (платформенные и фича-команды) | В3, 51 + уточнение пользователя 2026-10-30 | нет в CV | подтверждено пользователем |
| Галерея Stream Vision 2 | динамическая сетка 3–5 колонок | В18, 260 | нет в CV | только интервью |
| Промо-чипы Mega Chips | 5–10 элементов | В26, 379 | нет в CV | только интервью |
| Design Review | 20 разработчиков (В26); ~20–30 iOS-инженеров на общем Design Review (В45) | В26, 381; В45, 662 | нет в CV | только интервью |
| Закрытие техдолга виджета | ~1,5 года | В6, 99 | нет в CV | только интервью |
| Языки локализации | 3–8 европейских языков | В22, 308 | нет в CV | только интервью |
| Deep links | 20–30 сценариев | В21, 288 | нет в CV | только интервью |
| Опыт | 8 лет (2018–2026) | В1, 3–6 | CV: «7+ лет» | согласовано |
| Покрытие тестами на NDA2 | 13% → 75% | подтверждение пользователя 2026-11-02; `achievements.md` A2 | CV/банк: 13% → 75% | решено – 17% из В32 не использовать |
| Visitor Management | ~1 год разработки при меняющихся требованиях | В41, 596; В50, 732 | нет в CV | только интервью |
| Story Points | 3 SP ≈ 1 рабочий день; декомпозиция выше 5–8 SP | В43, 620–623 | нет в CV | только интервью |
| Раскатка по процентам | 5% → 20% пользователей | В27, 406 | нет в CV | только интервью |
| Phased Release | наблюдение на 1–5% пользователей | В35, 537 | нет в CV | только интервью |
| Релизный цикл NDA1 | 2 недели | В35, 537 | нет в CV | только интервью |
| Предупреждения SwiftLint на NDA2 | несколько тысяч накопленных | В34, 517 | нет в CV | только интервью |
| Crash-free на NDA2 | 99%+ | В35, 539 | CV: 99,8% (`achievements.md` A3) | согласуется |
| Митапы по Mock API | 2: внутренний и общекорпоративный | В51, 747 | CV: «серия митапов» | частично |
| Программа обучения Orangesoft | 3 студента, 2 трудоустроены | В48, 703 | нет в CV | только интервью |
| Reskilling в ISsoft | 1 коллега из QA до уровня Junior | В48, 702 | нет в CV | только интервью |
| Практика AI-SDLC | более года (NDA2 + пет-проект) | В62, 961 | master-cv: AI-assisted SDLC упомянут обобщённо | подтверждено |
| AI-SDLC lifecycle | 7 фаз | В62, 967 | нет в CV | только интервью |
| Always-loaded AGENTS.md router | ~9 КБ → ~2,4 КБ | В62, 977 | нет в CV | только интервью |
| Core trio документов | сокращение на 42% | В62, 977 | нет в CV | только интервью |
| Порог promotion паттерна в skill | 3 успешных применения | В62, 979 | нет в CV | только интервью |
| AI-адаптеры harness | Cursor, Claude Code, Codex | В62, 973 | master-cv: Cursor, Codex, GitHub Copilot | частично (Claude Code – только интервью) |

## AI-SDLC: что именно подтверждено (В62)

- **Контракт до кода:** SPEC.md (requirements с ID, бинарные acceptance criteria, non-goals, риски, privacy/analytics/accessibility/release impact) и PLAN.md (задачи по слоям, test strategy с mapping на требования, verification gates, rollout/rollback); оба утверждает человек.
- **Lifecycle:** Research → Plan → Execute → Quality Automation → Validate → Merge/Deploy/Telemetry → Refine; зелёный build – quality evidence, а не acceptance validation.
- **Границы агента:** может писать код, коммитить, пушить, открывать PR, отвечать на review; не может мержить, approve PR, ставить release tag, пушить в develop/main, деплоить, отменять quality gate, менять scope.
- **Evidence before done:** focused test, UI test, build, static inspection, manual observation или risk review на каждый acceptance criterion; недоступная проверка – видимое ограничение, bounded exception принимает человек.
- **Harness:** правила, шаблоны, skills, memory, ADR в Git; Cursor / Claude Code / Codex – адаптеры; zero install из свежего clone.
- **Multi-agent:** lead + research / implementation / review; параллелятся read-only research, независимый review и partitioned implementation по non-overlapping paths; не параллелятся общий SPEC/PLAN, project file, миграции, generated artifacts, state machine.
- **Context engineering:** search before reading, line ranges, narrowest test first, one skill per framework, smallest sufficient model, stop after two failed attempts.
- **Feedback loop:** Refine → memory (decisions / patterns / anti-patterns), ADR, feature journals, skills; skill после трёх успешных применений, promotion в policy – человек.
- **Результат за год:** ускорение Research/Plan против «догадок агента + переделок», раннее выявление упавших gates, evidence в каждом PR, знания в memory/ADR/skills, human-owned merge/deploy/release. Цифр ускорения в источнике нет.

## Цифры только в CV / банке (в интервью нет или значение отличается)

| Факт | Значение | Источник | Примечание |
|---|---|---|---|
| DAU платформы | 160K+ | `achievements.md` A3; `master-cv-ru.md` | использовать как есть |
| DAU приложения | 500K+ | `achievements.md` A4; `master-cv-ru.md` | использовать как есть |
| Crash-free rate | 99,8% | `achievements.md` A3; `master-cv-ru.md` | использовать как есть |
| Покрытие тестами | 13% → 75% | `achievements.md` A2; `master-cv-ru.md` | подтверждено 2026-11-02; 17% из В32 не использовать |
| Рейтинг Stream Vision 2 | 4,7/5, 1,2K оценок | `achievements.md` A5 (App Store, verified 2026-10-20) | использовать как есть |
| Сохранение функциональности после RxSwift → Combine | 100% | `master-cv-ru.md` | использовать как есть |
| Команда NDA2 | 4 iOS-инженера | `master-cv-ru.md` | решено: использовать 4 (см. `weak-notes.md`) |
| Команда Stream Vision 2 | 2 iOS-инженера | `master-cv-ru.md`; `achievements.md` A5 | использовать как есть |

## Правила

- Цифра, которой нет ни здесь, ни в CV/банке, не используется. Нужна – спросить пользователя.
- «Только интервью» не значит «можно усилить»: значение и смысл переносятся дословно.
- Расхождения не решать самостоятельно: фиксировать в `topics/weak-notes.md` и спрашивать.
