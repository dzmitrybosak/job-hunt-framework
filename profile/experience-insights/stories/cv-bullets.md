# CV-готовые bullets из интервью

Источник: `profile/self-interview.md` (**только чтение**). Привязка: компания / проект / даты из `profile/master-cv-ru.md` и `profile/master-cv-en.md`. Смысл и цифры – дословно, источник в комментарии `<!-- В<N> -->`.

Формат: `[action verb] + [scope/scale] + [result with number] + [tool/method]` (`prompts/achievement-bullets.md`), factual-тон, без successfully/efficiently.

Использование: `prompts/tailor-resume.md`, шаг 1a (уровень 2, рядом с Experience) → блок Key achievements. Нарративные `stories/star-stories.md` в резюме НЕ вставляются – они для cover letter и драфтов.

Это **пул кандидатов**, а не готовое резюме: под конкретную вакансию из каждого проекта отбираются 5–7 самых релевантных булетов (`prompts/tailor-resume.md`, шаг 2), остальное уходит в «Что изменилось / опущено».

Обозначения проектов: **NDA1** – Платформа управления недвижимостью и доступом (Октябрь 2021 – февраль 2024), **NDA2** – Платформа управления доступом (Февраль 2024 – Октябрь 2026). Как в интервью; в `master-cv` оба проекта идут с пометкой (NDA).

Статус: RU подтверждён 2026-11-04 (62 вопроса, включая блок В62); EN подтверждён 2026-11-04 (включая блок В62). Предыдущая версия RU/EN была подтверждена 2026-10-30.

Обновлено: 2026-11-04 (62 вопроса интервью; добавлен блок AI-SDLC по В62). Лимит 5–7 булетов действует на этапе tailoring (`resume-adapted`), а не на этом пуле кандидатов.

---

## RU (для master-cv-ru)

Статус: подтверждено 2026-11-02.

### Coherent Solutions (ISsoft) – Senior iOS-разработчик (Октябрь 2021 – Октябрь 2026)

#### Платформа управления доступом (NDA2) (Февраль 2024 – Октябрь 2026)

- Спроектировал Mock API (Demo Mode) поверх общего сетевого слоя: запросы (GET, POST и др.) перехватываются и возвращают JSON-фикстуры из локальных файлов, сделав тестирование и демо независимыми от бэкенда. <!-- В4 -->
- Реализовал виджет с интеграцией Siri и Shortcuts: открытие дверей и устройств свёл к одному тапу или голосовой команде, обеспечив мгновенную реакцию в ограничениях виджета по памяти и времени выполнения. <!-- В5 -->
- Параллелизировал загрузку стартовых данных (профиль, устройства, конфигурация главного экрана, уведомления) через TaskGroup, сократив холодный старт до времени самого долгого запроса; ошибки второстепенных запросов изолированы внутри группы. <!-- В16 -->
- Вынес чтение Keychain и сортировку избранных устройств для Siri в Task.detached, чтобы тяжёлая работа с хранилищем не задевала главный поток. <!-- В16 -->
- Устранил data race в параллельно выполняемых Unit-тестах, переведя Mock API Manager на actor. <!-- В14, В15 -->
- Перевёл внутреннюю библиотеку нетворкинга и работы с устройствами с completion handlers на async/await через withCheckedContinuation, сохранив обратную совместимость старого кода. <!-- В14 -->
- Мигрировал дата-координаторы (enum со статическими методами) на объекты с initializer injection, сделав зависимости явными и разблокировав написание Unit-тестов. <!-- В25 -->
- Оптимизировал локализацию: провёл ревизию базы строк, удалил дубликаты, внедрил системный нейминг ключей и перевёл проект на String Catalogs. <!-- В22 -->
- Внедрил поддержку VoiceOver (accessibilityLabel / accessibilityHint / accessibilityIdentifier) и Dynamic Type, добавил в PR-шаблон чек-лист проверки языков и размеров шрифта. <!-- В22 -->
- Закрыл техдолг виджета спустя ~1,5 года: дублированный в таргете виджета координатор заменён переиспользуемой логикой при переходе на SPM-модули и Clean Architecture. <!-- В6 -->
- Реализовал SSO через WebView: токены Access и Refresh хранятся в Keychain, сессия обновляется на холодном старте, при истечении сессии корневое view переключается на экран логина. <!-- В21 -->
- Реализовал адаптивную навигацию iPad (Sidebar / Content / Detail) на Tab View и NavigationView / NavigationLink, включая обработку Deep Links внутри модулей. <!-- В21 -->
- Синхронизировал архитектурное видение решений с Android-разработчиком до написания кода и согласовывал его с лидом / Product Owner для консистентности обеих платформ. <!-- В3 -->
- Мигрировал модуль с UIKit на SwiftUI: экраны профиля и настроек, динамические списки с пагинацией, формы, графики и кастомные контролы; управление состоянием на @State / @Binding, ObservableObject + @Published, EnvironmentObject, на последнем проекте – макрос @Observable. После перевода последнего UIKit-модуля из проекта удалили все импорты UIKit; интероп с UIKit остался единичным. <!-- В19, В27 -->
- Подключал UIKit-компоненты в SwiftUI через UIViewRepresentable / UIViewControllerRepresentable, включая UIActivityViewController для системного шаринга. <!-- В19, В20 -->
- Унифицировал показ тостов через протокол Toastable с реализацией по умолчанию: любая ViewModel вызывала отображение ошибок и успехов через расширение протокола. <!-- В10 -->
- Разрабатывал модуль Visitor Management около года при постоянно меняющихся требованиях: декомпозировал задачи на себя и помогающего коллегу, синхронизировался с Web-командой и бизнесом, фиксировал договорённости в Jira и Confluence. <!-- В41, В50 -->
- Довёл покрытие Unit-тестами с 13% до 75%: провёл аудит покрытия по слоям и модулям, обосновал план перед бизнесом и командой. <!-- В32 -->
- Внедрил Swift Testing как основной стандарт тестирования: провёл для команды мастер-класс по миграции с XCTest. <!-- В32, В51 -->
- Покрыл SwiftUI-компоненты Unit-тестами через ViewInspector и добавил Snapshot-тесты на SnapshotTesting для стабильности вёрстки. <!-- В32 -->
- Восстановил SwiftLint после долгого перерыва: обработал несколько тысяч накопленных предупреждений и ошибок, настроил блокировку мержа по критическим нарушениям. <!-- В34 -->
- Реализовал token refresh с очередью запросов: при 401 ожидающие вызовы приостанавливались, токен обновлялся, запросы повторялись автоматически. <!-- В28 -->
- Провёл миграцию структуры данных устройств в Keychain (массив → словарь) с ручным кодом миграции, сохранив данные пользователей при обновлении. <!-- В29 -->
- Реализовал синхронизацию iPhone и Apple Watch: iPhone как единственный источник истины, часы получают актуальное состояние при восстановлении связи. <!-- В29, В30 -->
- Реализовал offline-поведение экранов: кэш последних данных, skeleton-анимация при обновлении, заглушка без сети, отслеживание состояния через NWPathMonitor. <!-- В30 -->
- Внедрил чек-лист для Pull Request и настоял на дроблении крупных PR на атомарные части, сократив время ревью и повысив глубину анализа кода. <!-- В46 -->
- Участвовал в формировании Definition of Done из шести пунктов: требования, качество кода и ревью, unit-тесты, продуктовые метрики, локализация, CI. <!-- В45 -->
- Исполнял роль Scrum-мастера в рамках недельной ротации: вёл Daily и другие ритуалы, удерживал повестку и фиксировал блокеры. <!-- В46 -->
- Внедрил и больше года развиваю spec-first, decision-first AI-SDLC на коммерческом iOS-проекте (NDA2) и в пет-проекте: перед реализацией создаются SPEC.md (requirements с ID, бинарные acceptance criteria, non-goals, риски, privacy/analytics/accessibility/release impact) и PLAN.md (задачи по слоям, test strategy с mapping на требования, verification gates, rollout/rollback), которые утверждает человек. <!-- В62 -->
- Выстроил 7-фазный lifecycle – Research → Plan → Execute → Quality Automation → Validate → Merge/Deploy/Telemetry → Refine – с запретом пропускать фазу через переименование работы: зелёный build считается quality evidence, а не acceptance validation. <!-- В62 -->
- Разграничил ответственность агента и человека: агент пишет код, коммитит, пушит, открывает PR и отвечает на review; merge, approve PR, release tag, push в develop/main, deploy, отмена quality gate и изменение scope остаются за человеком. <!-- В62 -->
- Ввёл evidence before done: каждый acceptance criterion подтверждается focused test, UI test, build, static inspection, manual observation или risk review; упавшая или недоступная проверка фиксируется как ограничение, а bounded exception принимает только человек. <!-- В62 -->
- Сделал tool-neutral harness в Git: правила, шаблоны, skills, memory и ADR хранятся в репозитории, Cursor, Claude Code и Codex подключаются как адаптеры, а свежий clone содержит всё необходимое для работы. <!-- В62 -->
- Оркестрировал multi-agent работу с lead и ролями research / implementation / review: параллелил read-only research, независимый review и partitioned implementation по non-overlapping paths, не параллеля общий SPEC/PLAN, project file, миграции и generated artifacts; lead отвечал за combined diff и повторную verification. <!-- В62 -->
- Сократил always-loaded AGENTS.md router с ~9 КБ до ~2,4 КБ и core trio на 42%, вынеся детали в scoped docs; закрепил search before reading, line ranges вместо целых файлов, narrowest test first, smallest sufficient model и остановку после двух неудачных попыток. <!-- В62 -->
- Замкнул feedback loop: Refine переводит delivery evidence в memory (decisions / patterns / anti-patterns), ADR, feature journals и skills; повторяющийся паттерн становится skill после трёх успешных применений, а promotion в policy решает человек. <!-- В62 -->

#### Платформа управления недвижимостью и доступом (NDA1) (Октябрь 2021 – февраль 2024)

- Спроектировал Data Driven UI промо-чипов: контент (5–10 элементов) управляется через Remote Config, при недоступном конфиге показывается дефолтный набор, состояния Loading / Success / Error вынесены в state machine. <!-- В26 -->
- Презентовал архитектуру модуля на Design Review для команды из 20 разработчиков, получив фидбек на раннем этапе и избежав конфликтов в навигации. <!-- В26 -->
- Управлял длинными флоу подключения устройств через Flow Controller: массив контроллеров в цепочке позволял сбросить стек, вернуться на конкретный шаг или перезапустить флоу. <!-- В21 -->
- Поддерживал 20–30 сценариев Deep Links, программно выстраивая путь навигации, чтобы возврат назад оставался корректным. <!-- В21 -->
- Перевёл UI с Storyboards/XIB на вёрстку кодом и участвовал в развитии дизайн-системы: переиспользуемые лейблы, кнопки и кастомные вью по общим гайдлайнам. <!-- В18 -->
- Спроектировал модели карточек Remote Config на протоколах с реализацией по умолчанию, чтобы новые типы карточек получали логику парсинга без дублирования кода. <!-- В10 -->
- Провёл глубокую декомпозицию legacy-контроллера, свёрстанного на Storyboard: аргументировал Product Owner-у, что текущая структура не позволит реализовать рекламный модуль и тултипсы с нужным качеством. <!-- В27 -->
- Раскатывал функционал поэтапно: включал изменения сначала на 5%, затем на 20% пользователей, отслеживая метрики и краши перед релизом на всю аудиторию. <!-- В27 -->
- Работал в практике выделения процента ёмкости спринта на техдолг: подсвечивал проблемные места тимлиду, которая согласовывала их с Product Owner; каждое TODO фиксировал отдельным тикетом в Jira. <!-- В47 -->
- Отслеживал стабильность билда в двухнедельном релизном цикле с Phased Release на 1–5% пользователей и останавливал раскатку при аномалиях в аналитике. <!-- В35 -->
- Выпускал хотфиксы через отдельные ветки под исправление с обязательным backmerge в основные ветки разработки, чтобы избежать регрессий. <!-- В35 -->
- Работал с биометрией Face ID и Touch ID через LocalAuthentication в общем флоу авторизации. <!-- В39 -->
- Применял обфускацию перед каждым релизом и участвовал в реализации генерации динамических ключей с проверкой на бэкенде для верификации оригинального приложения. <!-- В39 -->
- Участвовал в миграции CI с Azure DevOps на GitHub Actions: более мощные машины ускорили сборку и снизили затраты. <!-- В33 -->
- Исправлял Code Smells и уязвимости по отчётам SonarQube; quality gates блокировали мерж при падении покрытия тестами или росте дублирования кода. <!-- В34 -->

### Orangesoft Development – iOS-разработчик (Январь 2019 – октябрь 2021)

#### Stream Vision 2 (Ноябрь 2019 – Октябрь 2021)

- Создал Trim View для обрезки видео с нуля: лента кадров, кастомные ползунки границ и жесты через UIGestureRecognizer; комбинация Auto Layout с ручным расчётом фреймов сохранила плавный скролл видеоряда. <!-- В18 -->
- Выстроил навигацию на координаторах: AppCoordinator и дочерние координаторы управляли внедрением зависимостей и жизненным циклом экранов, вынося переходы из ViewControllers. <!-- В21 -->
- Реализовал очередь загрузки и выгрузки данных в облако на OperationQueue: зависимости между операциями, контроль параллелизма и явная отмена устаревших задач. <!-- В14 -->
- Реализовал динамическую сетку галереи на 3–5 колонок с пересчётом размеров ячеек на лету, внедрив prefetching и оптимизацию prepareForReuse для плавного скролла. <!-- В18 -->
- Адаптировал экран управления устройством под портрет и ландшафт через приоритеты констрейнтов и динамические константы: вертикальный стек в портрете, горизонтальное расположение кнопок в ландшафте, без конфликтов констрейнтов в логах. <!-- В18; проект подтверждён пользователем -->
- Перевёл экран настроек с кастомной логики двух панелей на UISplitViewController, обеспечив нативную поддержку iPhone и iPad в обеих ориентациях. <!-- В18; проект подтверждён пользователем -->
- Полностью отвечал за внедрение и настройку Bitrise: сборка, прогон тестов, доставка в TestFlight и уведомления в Telegram. <!-- В33 -->
- Выстроил конфигурацию SwiftLint с нуля, балансируя строгость правил и удобство разработки. <!-- В34 -->
- Стал первым, кто начал системно внедрять Unit-тестирование в проекте: покрывал бизнес-логику через моки, стабы и Dependency Injection. <!-- В32 -->
- Инициировал и реализовал Quick Actions для иконки приложения, сократив путь пользователя к ключевым функциям. <!-- В40 -->
- Провёл очистку проекта от dead code и неиспользуемых ресурсов, аудит ассетов и оптимизацию размера бандла без потери функциональности. <!-- В38 -->
- Реализовал локальное хранилище на Core Data через обёртку CoreStore, упростив многопоточность и работу с контекстами. <!-- В29 -->
- Полностью курировал онбординг нового junior-разработчика: архитектуру системы, логику фич и стандарты кода проекта. <!-- В54, В61 -->

#### Остальные проекты (Январь – ноябрь 2019)

##### Стрелковый союз

- Реализовал модуль календаря мероприятий на VIPER, инкапсулировав навигацию в роутерах. <!-- В21, В23 -->

##### WineBeMine

- Интегрировал StoreKit и реализовал систему подписок с серверной валидацией чеков (Receipt Validation) и восстановлением покупок (Restore Purchases), синхронизировав статусы оплаты с бэкенд-командой. <!-- В35, В56 -->

##### MobiScan

- Реализовал сохранение PDF-чеков, генерируемых из UI, через FileManager. <!-- В29 -->
- Использовал Vision для задач сканирования. <!-- В56 -->
- Провёл серию Knowledge Transfer-сессий при передаче проекта другому разработчику, объяснив внутреннее устройство приложения для последующей переработки. <!-- В54 -->

##### Realt

- Участвовал в глубоком аудите legacy-кодовой базы и поэтапном переписывании критических узлов при рассинхронизации старого и нового бэкендов, что позволило стабилизировать отдельные модули. <!-- В54 -->
- Реализовал сложную логику выбора зон поиска недвижимости по полигонам на Yandex Maps SDK. <!-- В56 -->
- Интегрировал MapKit и CoreLocation: системные карты, аннотации и геопозицию пользователя. <!-- В56 -->

Merry Kitchen – в интервью упоминается только использование Realm; отдельные bullets не добавляются.

---

## EN (для master-cv-en)

Статус: подтверждён 2026-11-04 (62 вопроса, включая блок В62).

### Coherent Solutions (ISsoft) – Senior iOS Developer (October 2021 – October 2026)

#### Access Management Platform (NDA2) (February 2024 – October 2026)

- Designed a Mock API (Demo Mode) on top of the shared networking layer: requests (GET, POST, etc.) are intercepted and served from local JSON fixtures, making testing and demos independent of the backend. <!-- В4 -->
- Built the widget with Siri and Shortcuts integration, reducing door and device access to a single tap or voice command, with instant response under widget memory and execution time constraints. <!-- В5 -->
- Parallelized app launch data loading (profile, devices, home screen configuration, notifications) via TaskGroup, cutting cold start time to that of the slowest request, with failures of secondary requests isolated inside the group. <!-- В16 -->
- Moved Keychain reads and favorite-device sorting for Siri into Task.detached so heavy storage work never touches the main thread. <!-- В16 -->
- Eliminated a data race in parallel unit tests by porting the Mock API Manager to an actor. <!-- В14, В15 -->
- Migrated the internal networking and device communication library from completion handlers to async/await using withCheckedContinuation, keeping backward compatibility with legacy code. <!-- В14 -->
- Migrated data coordinators (enums with static methods) to objects with initializer injection, making dependencies explicit and unlocking unit testing. <!-- В25 -->
- Optimized localization: audited the string base, removed duplicates, introduced consistent key naming, and moved the project to String Catalogs. <!-- В22 -->
- Shipped VoiceOver support (accessibilityLabel / accessibilityHint / accessibilityIdentifier) and Dynamic Type, and added language and font-size checks to the PR template. <!-- В22 -->
- Closed the widget tech debt ~1.5 years later: the duplicated widget-target coordinator was replaced with reusable logic during the migration to SPM modules and Clean Architecture. <!-- В6 -->
- Implemented SSO via WebView with Access and Refresh tokens stored in Keychain, session refresh on cold start, and a root view switch to the login screen when the session expires. <!-- В21 -->
- Implemented adaptive iPad navigation (Sidebar / Content / Detail) on Tab View and NavigationView / NavigationLink, including deep link handling inside modules. <!-- В21 -->
- Aligned the architectural design with the Android engineer before implementation and reviewed it with the tech lead / Product Owner to keep both platforms consistent. <!-- В3 -->
- Migrated a module from UIKit to SwiftUI: profile and settings screens, paginated dynamic lists, forms, charts and custom controls; state managed with @State / @Binding, ObservableObject + @Published, EnvironmentObject, and the @Observable macro on the latest project. After migrating the last UIKit module, all UIKit imports were removed from the project; UIKit interop remained only in isolated cases. <!-- В19, В27 -->
- Embedded UIKit components in SwiftUI via UIViewRepresentable / UIViewControllerRepresentable, including UIActivityViewController for system sharing. <!-- В19, В20 -->
- Unified toast presentation through the Toastable protocol with a default implementation, so any ViewModel could show errors and success states via the protocol extension. <!-- В10 -->
- Worked on the Visitor Management module for about a year under constantly changing requirements: split tasks between myself and a supporting colleague, stayed in sync with the Web team and business, and recorded agreements in Jira and Confluence. <!-- В41, В50 -->
- Raised unit test coverage from 13% to 75%: audited coverage by layer and module and made the case for the plan to business and the team. <!-- В32 -->
- Adopted Swift Testing as the primary testing standard and ran a masterclass for the team on migrating from XCTest. <!-- В32, В51 -->
- Covered SwiftUI components with unit tests via ViewInspector and added snapshot tests on SnapshotTesting to keep layout stable. <!-- В32 -->
- Restored SwiftLint after a long gap: resolved several thousand accumulated warnings and errors and set up merge blocking on critical violations. <!-- В34 -->
- Implemented token refresh with a request queue: pending calls paused on 401, the token refreshed, and requests retried automatically. <!-- В28 -->
- Migrated the device data structure in Keychain (array to dictionary) with hand-written migration code, preserving user data across app updates. <!-- В29 -->
- Implemented iPhone and Apple Watch synchronization: iPhone as the single source of truth, with the watch receiving current state when connectivity returns. <!-- В29, В30 -->
- Implemented offline screen behavior: cached last data, skeleton animation during refresh, an informative no-network state, and connectivity tracking via NWPathMonitor. <!-- В30 -->
- Introduced a Pull Request checklist and pushed for splitting large PRs into atomic parts, cutting review time and deepening code analysis. <!-- В46 -->
- Co-defined a six-point Definition of Done: requirements, code quality and review, unit tests, product analytics, localization, and CI. <!-- В45 -->
- Rotated as Scrum Master for a week at a time: ran the Daily and other ceremonies, kept the agenda on track, and logged blockers. <!-- В46 -->
- Introduced a spec-first, decision-first AI-SDLC and have been running it for over a year on a commercial iOS product (NDA2) and in a pet project: before any implementation, SPEC.md (requirements with IDs, binary acceptance criteria, non-goals, risks, privacy/analytics/accessibility/release impact) and PLAN.md (layer-based tasks, test strategy mapped to requirements, verification gates, rollout/rollback) are created and approved by a human. <!-- В62 -->
- Built a seven-phase lifecycle – Research → Plan → Execute → Quality Automation → Validate → Merge/Deploy/Telemetry → Refine – where a phase cannot be skipped by renaming its work: a green build counts as quality evidence, not acceptance validation. <!-- В62 -->
- Separated agent and human responsibilities: the agent writes code, commits, pushes, opens PRs and responds to review; merge, PR approval, release tags, pushes to develop/main, deploys, overrides of failed quality gates and scope changes remain human-owned. <!-- В62 -->
- Introduced evidence before done: every acceptance criterion gets concrete evidence through a focused test, UI test, build, static inspection, manual observation or risk review; a failed or unavailable check is recorded as a visible limitation, and only a human can accept a bounded exception. <!-- В62 -->
- Built a tool-neutral harness in Git: rules, templates, skills, memory and ADRs live in the repository, Cursor, Claude Code and Codex connect as adapters, and a fresh clone contains everything needed to work. <!-- В62 -->
- Orchestrated multi-agent work with a lead and research / implementation / review roles: ran read-only research, independent review and partitioned implementation over non-overlapping paths in parallel, while never parallelizing the shared SPEC/PLAN, project file, migrations or generated artifacts; the lead owned the combined diff and re-verification. <!-- В62 -->
- Reduced the always-loaded AGENTS.md router from ~9 KB to ~2.4 KB and the core trio by 42% by moving details into scoped docs; established search before reading, line ranges instead of whole files, narrowest test first, the smallest sufficient model, and stopping after two failed attempts. <!-- В62 -->
- Closed the feedback loop: Refine turns delivery evidence into durable improvements in memory (decisions / patterns / anti-patterns), ADRs, feature journals and skills; a recurring pattern becomes a skill only after three successful applications, and promotion into policy stays human-owned. <!-- В62 -->

#### Property & Access Management Platform (NDA1) (October 2021 – February 2024)

- Designed the Data Driven UI for the promo chips module: content (5–10 items) is driven by Remote Config with a hardcoded fallback, and Loading / Success / Error states live in a state machine. <!-- В26 -->
- Presented the module architecture at a Design Review for a team of 20 developers, capturing feedback early and avoiding navigation conflicts. <!-- В26 -->
- Managed long device-connection flows with a Flow Controller: an array of view controllers in a chain allowed resetting the stack, jumping back to a specific step, or restarting the flow. <!-- В21 -->
- Supported 20–30 deep link scenarios by programmatically building the navigation path so back navigation stays correct. <!-- В21 -->
- Moved the UI from Storyboards/XIB to code-based layout and contributed to the design system: reusable labels, buttons and custom views following shared guidelines. <!-- В18 -->
- Designed Remote Config card models on protocols with default implementations, so new card types inherited parsing logic without code duplication. <!-- В10 -->
- Decomposed a legacy Storyboard view controller, making the case to the Product Owner that the existing structure could not support the ad module and tooltips at the required quality bar. <!-- В27 -->
- Rolled out functionality in stages: enabled changes for 5% and then 20% of users, watching metrics and crashes before the full release. <!-- В27 -->
- Worked within a practice of allocating a share of sprint capacity to tech debt: raised problem areas with the tech lead, who aligned them with the Product Owner, and logged every TODO as a separate Jira ticket. <!-- В47 -->
- Monitored build stability in a two-week release cycle with Phased Release on 1–5% of users and paused the rollout on analytics anomalies. <!-- В35 -->
- Shipped hotfixes through dedicated fix branches with a mandatory backmerge into the main development branches to prevent regressions. <!-- В35 -->
- Worked with Face ID and Touch ID via LocalAuthentication in the shared authorization flow. <!-- В39 -->
- Applied obfuscation before every release and contributed to dynamic key generation verified on the backend to confirm requests came from the original app. <!-- В39 -->
- Took part in the CI migration from Azure DevOps to GitHub Actions, where more powerful machines sped up builds and reduced costs. <!-- В33 -->
- Fixed Code Smells and vulnerabilities from SonarQube reports; quality gates blocked merges on falling test coverage or rising code duplication. <!-- В34 -->

### Orangesoft Development – iOS Developer (January 2019 – October 2021)

#### Stream Vision 2 (November 2019 – October 2021)

- Built the Trim View video editing screen from scratch – frame thumbnails, custom range sliders, and UIGestureRecognizer-driven logic; mixing Auto Layout with manual frame layout kept the frame strip smooth while scrolling. <!-- В18 -->
- Built navigation on coordinators: AppCoordinator and child coordinators handled dependency injection and view controller lifecycles, keeping navigation out of view controllers. <!-- В21 -->
- Implemented the cloud upload and download queue on OperationQueue with operation dependencies, bounded concurrency, and explicit cancellation of stale tasks. <!-- В14 -->
- Built a dynamic gallery grid of 3–5 columns with on-the-fly cell sizing, adding prefetching and prepareForReuse optimization to keep scrolling smooth. <!-- В18 -->
- Adapted the device control screen for portrait and landscape using constraint priorities and dynamic constants: a vertical stack in portrait, horizontally rearranged buttons in landscape, with no constraint conflicts in the logs. <!-- В18; project confirmed by the user -->
- Replaced the custom two-pane settings logic with UISplitViewController, providing native support for iPhone and iPad in both orientations. <!-- В18; project confirmed by the user -->
- Owned the Bitrise setup end to end: build, test run, TestFlight delivery, and Telegram notifications. <!-- В33 -->
- Built the SwiftLint configuration from scratch, balancing rule strictness against day-to-day developer convenience. <!-- В34 -->
- Was the first to introduce unit testing systematically on the project, covering business logic with mocks, stubs, and dependency injection. <!-- В32 -->
- Initiated and shipped Quick Actions for the app icon, shortening the path to key features. <!-- В40 -->
- Cleaned the project of dead code and unused resources, audited assets, and optimized the bundle size without losing functionality. <!-- В38 -->
- Implemented local storage on Core Data through the CoreStore wrapper, simplifying multithreading and context management. <!-- В29 -->
- Fully owned the onboarding of a new junior developer: system architecture, feature logic, and the project's coding standards. <!-- В54, В61 -->

#### Other projects (January – November 2019)

##### Shooting Union

- Implemented the event calendar module in VIPER with navigation encapsulated in routers. <!-- В21, В23 -->

##### WineBeMine

- Integrated StoreKit and built the subscription system with server-side receipt validation and Restore Purchases, syncing payment statuses with the backend team. <!-- В35, В56 -->

##### MobiScan

- Implemented saving of PDF receipts generated from the UI via FileManager. <!-- В29 -->
- Used Vision for scanning tasks. <!-- В56 -->
- Ran a series of knowledge transfer sessions when handing the project to another developer, explaining the app's internals ahead of its rework. <!-- В54 -->

##### Realt

- Took part in a deep audit of the legacy codebase and the phased rewrite of critical nodes amid desynchronized old and new backends, which helped stabilize individual modules. <!-- В54 -->
- Implemented complex property search area selection by polygons on the Yandex Maps SDK. <!-- В56 -->
- Integrated MapKit and CoreLocation: system maps, annotations, and user location. <!-- В56 -->

Merry Kitchen has only a Realm mention in the interview, so no separate bullets are added.

---

## Внепроектная деятельность (все подтверждённые факты, вне лимита 5–7)

### RU (для master-cv-ru)

Статус: подтверждено 2026-11-02.

#### Coherent Solutions (ISsoft) – Senior iOS-разработчик (Октябрь 2021 – Октябрь 2026)

Из `master-cv-ru.md` (дословно):

- Выступал в роли тренера во внутреннем учебном центре на курсе Swift & iOS: сопровождал стажеров по программе обучения и объяснял сложные технические концепции.
- Регулярно проводил ревью кода для студентов и занимался менторством, обеспечивая успешное завершение курса.
- Участвовал в качестве технического интервьюера, проводя оценку кандидатов на инженерные позиции внутри компании.
- Инициировал и провел серию технических митапов внутри проекта и на уровне компании по темам миграции с XCTest на Swift Testing и внедрения Mock-слоя для нетворкинга.

Из интервью:

- Проводил демо на аудиторию 100+ человек. <!-- В2 -->
- Довёл коллегу из тестирования до уровня Junior по программе reskilling; сейчас она работает в штате. <!-- В48 -->
- Инициировал обмен опытом внутри iOS-команды по AI-инструментам: практические кейсы, промпты и инструменты. <!-- В51 -->
- Создавал детальную документацию по ключевым разработкам (например, Mock API) в Confluence и в коде, чтобы новые разработчики быстрее включались в процесс. <!-- В48 -->

Детали к булетам выше (при сборке резюме объединять, не дублировать):

- Провёл два митапа по собственной библиотеке Mock API: внутренний для команды проекта и общекорпоративный. <!-- В51 -->
- Проводил технические интервью кандидатов уровней Middle и Senior: техническая секция, live coding и system design, подробный письменный фидбек в специализированной форме. <!-- В49 -->

#### Orangesoft Development – iOS-разработчик (Январь 2019 – октябрь 2021)

Из `master-cv-ru.md` (дословно; в митап-булет влита деталь В7):

- Менторил группу стажеров: разрабатывал планы обучения (roadmaps), распределял проектные задачи, проводил глубокое ревью кода и предоставлял конструктивную обратную связь.
- Участвовал в процессе технического найма, проводя интервью с потенциальными кандидатами в компанию.
- Организовал и провел внутренние технические митапы по развитию Swift и iOS стека, посвященные новым версиям (включая митап про Swift 5.0 и ABI stability), помогая коллегам быстрее адаптироваться к изменениям API. <!-- В7: тема митапа влита в bullet -->

Из интервью:

- Разработал с коллегой с нуля программу обучения студентов: курировал трёх человек от теории до практических заданий и code review; двое из трёх трудоустроены в компанию. <!-- В48 -->

### EN (для master-cv-en)

Статус: подтверждён 2026-11-04 (62 вопроса, включая блок В62).

#### Coherent Solutions (ISsoft) – Senior iOS Developer (October 2021 – October 2026)

From `master-cv-en.md` (verbatim):

- Served as a Trainer at the internal Training Center for the Swift & iOS course, guiding trainees through the curriculum and explaining complex technical concepts.
- Conducted regular code reviews for students and provided mentorship to ensure successful course completion.
- Acted as a technical interviewer, evaluating candidates for engineering positions within the company.
- Initiated and led a series of technical meetups at both the project and company levels, focusing on migrating from XCTest to Swift Testing and implementing a networking mock layer.

From the interview:

- Ran product demos for audiences of 100+ people. <!-- В2 -->
- Took a colleague from QA to a Junior iOS level through a reskilling program; she now works on staff. <!-- В48 -->
- Initiated knowledge sharing on AI tooling within the iOS team: practical cases, prompts, and tools. <!-- В51 -->
- Created detailed documentation for key developments (such as Mock API) in Confluence and in code so new developers could get up to speed faster. <!-- В48 -->

Details for the bullets above (merge when building the resume, do not duplicate):

- Delivered two meetups on my own Mock API library: one for the project team and one company-wide. <!-- В51 -->
- Interviewed Middle and Senior candidates: technical section, live coding, and system design, with detailed written feedback in a dedicated form. <!-- В49 -->

#### Orangesoft Development – iOS Developer (January 2019 – October 2021)

From `master-cv-en.md` (verbatim; the meetup bullet has the В7 detail merged in):

- Mentored a pool of interns by designing learning roadmaps, assigning project tasks, and providing comprehensive code reviews and constructive feedback.
- Participated in the technical recruitment process by conducting interviews for prospective candidates.
- Organized and hosted internal technical meetups focused on Swift and iOS stack evolution, covering new releases (including a Swift 5.0 and ABI stability meetup) and helping colleagues accelerate their adaptation to API changes. <!-- В7: meetup topic merged into the bullet -->

From the interview:

- Co-designed a student training program from scratch: mentored three people from theory through hands-on assignments and code review; two of the three were hired by the company. <!-- В48 -->

---

## Не дублировать (уже в CV)

Факты, которые уже отражены в master-cv / банке achievements. Не добавлять повторно: если в интервью есть важная деталь этого же факта, добавлять её как деталь в существующий bullet, а не как отдельный дубликат:

- 1M+ взаимодействий виджета (A1, master-cv) – В5.
- RxSwift → Combine, 100% функциональности (master-cv) – В23.
- SPM-модули, MVVM, Clean Architecture (master-cv) – В23, В24.
- Mega Chips как компонент главного экрана (master-cv) – В26.
- Видеоредактор с обрезкой на AVFoundation (master-cv) – В18.
- Покрытие тестами 13% → 75% (master-cv, банк) – вынесено в bullet NDA2 с деталями аудита; подтверждено 2026-11-02, цифра 17% из В32 не использовать.
- Миграция UIKit → SwiftUI, Widgets / App Intents / Shortcuts (master-cv) – В19; полный уход от импортов UIKit добавлен как деталь в bullet NDA2 (В27).
- AI-assisted SDLC и spec-driven development (master-cv, NDA2) – В62; в пул добавлены детали процесса (SPEC/PLAN, 7 фаз, evidence, harness, orchestration, context engineering), а не дубликат общих формулировок.
- Merry Kitchen – в интервью только упоминание Realm; отдельных bullets нет.

## Журнал

- 2026-10-29: подтверждены RU/EN; deep links + Flow Controller → NDA1; EPAM – верны даты CV, в резюме не добавлять; демо 100+ и митап В7 → внепроектная деятельность.
- 2026-10-30: В17 («Мало опыта»); добавлены bullets В10/В18/В19/В20; NDA → NDA1/NDA2; команда – 4 инженера; новостное MVP в CV не добавляем; RU/EN подтверждены.
- 2026-10-30: экраны управления устройством и настроек (В18) → Stream Vision 2 (подтверждено пользователем); bullets добавлены, открытых вопросов по файлу нет.
- 2026-11-02: слой пересобран под 61 вопрос интервью. Добавлены bullets: NDA2 – Visitor Management, тесты 75%, Swift Testing, ViewInspector/Snapshot, SwiftLint, token refresh, Keychain-миграция, Watch, offline, PR-чек-лист, DoD, Scrum Master; NDA1 – legacy-контроллер, раскатка 5% → 20%, ёмкость на техдолг, двухнедельный цикл, hotfix + backmerge, биометрия, обфускация, CI-миграция, SonarQube; Stream Vision 2 – Bitrise, SwiftLint, первые unit-тесты, Quick Actions, dead code, CoreStore, онбординг junior; WineBeMine, MobiScan и realt.by получили отдельные блоки; внепроектка дополнена reskilling, митапами, AI-обменом, интервью и программой обучения Orangesoft. RU отправлен на подтверждение, EN – DRAFT.
- 2026-11-02: расхождения закрыты по ответам пользователя: покрытие тестами – верно 13% → 75%; импорты UIKit удалены из всего проекта после перевода последнего модуля, интероп остался единичным; Privacy Manifests внедрял только в пет-проекте.
- 2026-11-02: RU-секция подтверждена пользователем. EN остаётся DRAFT до отдельного подтверждения.
- 2026-11-04: добавлен В62 (AI-SDLC). В NDA2 добавлены 8 bullets RU и EN: SPEC.md/PLAN.md с human approval, 7-фазный lifecycle, границы агента и человека, evidence before done, tool-neutral harness в Git, multi-agent orchestration, context/token engineering (AGENTS.md ~9 КБ → ~2,4 КБ, core trio сокращён на 42%), feedback loop через memory/ADR/skills. Первый bullet явно фиксирует, что подход применялся более года на коммерческом проекте (NDA2) и в пет-проекте. Факт уже был в master-cv обобщённо, поэтому добавлены детали процесса, а не дубликат. RU-блок подтверждён 2026-11-04; EN – DRAFT.
- 2026-11-04: подтверждения пользователя. RU-блок В62 подтверждён; master-cv-ru/en дополнены AI-SDLC-булетами (SPEC/PLAN с human approval, 7-фазный lifecycle, границы агента/человека, evidence before done + harness + orchestration + context engineering) и общей фразой про более года практики на NDA2 и в пет-проекте; в achievements.md добавлен A6. EN-секция cv-bullets переведена из DRAFT в подтверждённую.
