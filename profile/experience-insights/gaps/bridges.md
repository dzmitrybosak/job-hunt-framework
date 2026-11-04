# Мосты: опыт из интервью → типовые гэпы вакансий

Как использовать: `gap-analysis.md` при ⚠️/❌ проверяет этот файл. Здесь – только то, что реально есть в `profile/self-interview.md`; формулировки не усилены. Для резюме брать факт и адаптировать лексику, не меняя смысл. Обновлено: 2026-11-04 (62 вопроса; раздел 12 расширен по В62).

## 1. Legacy и Objective-C

- **Что есть:** миграция `.h`/`.m` → Swift с сохранением поведения, Bridging Header, `@objc`/`dynamic`, понимание рантайма ObjC (S4; В12).
- **Закрывает:** «опыт поддержки/миграции legacy», «Objective-C», «понимание рантайма».
- **Ограничение:** не заявлять полную миграцию всего проекта и KVC/KVO-экспертизу – в интервью это описано как осторожное использование.

## 2. Swift Concurrency

- **Что есть:** поэтапная миграция completion handlers → async/await через `withCheckedContinuation`, `do-catch`, отмена задач (S6; В14); actor для Mock API Manager (S7; В14–15); TaskGroup в Launch Coordinator, `Task.detached` для Siri, приоритеты (S8; В16); Sendable-модели и Transition-модели (В15).
- **Закрывает:** «Swift Concurrency», «async/await», «actors», «structured concurrency», «data races».
- **Ограничение:** не приписывать миграцию всего проекта – только внутренняя библиотека и новый код.

## 3. Тестируемость и тестовая культура

- **Что есть:** Mock API для тестов без сети (S1; В4); actor для устранения data race в параллельных Unit-тестах (S7; В14–15); миграция со статических enum-координаторов на initializer injection, чтобы разблокировать тесты (S12; В25); аудит и рост 13% → 75% и обоснование перед бизнесом, мастер-класс XCTest → Swift Testing, ViewInspector и SnapshotTesting, тесты как обязательный шаг CI (S20; В32, В51).
- **Закрывает:** «unit-тесты», «snapshot-тесты», «SwiftUI-тестирование», «тестируемая архитектура», «DI для тестов», «моки», «внедрение тестовой культуры».
- **Ограничение:** цифра 17% из В32 ошибочна; использовать 13% → 75% (подтверждено 2026-11-02).

## 4. Модульная архитектура

- **Что есть:** SPM-модули Core/Feature, гибрид с CocoaPods для вендора, фича-флаги при миграции, подготовка к KMP (S13; В24); Clean Architecture и MVVM (В23).
- **Закрывает:** «модуляризация», «SPM», «Clean Architecture», «границы модулей».
- **Ограничение:** межмодульные зависимости через Core/координаторы не доведены до внедрения – говорить как о плане, не как о факте.

## 5. System / feature design

- **Что есть:** Mock API – ~месяц проектирования, переиспользование существующего сетевого слоя (S1; В4); Mega Chips – Data Driven UI, Remote Config, fallback, state machine, Design Review на 20 разработчиков (S10; В26).
- **Закрывает:** «system design», «проектирование фичи с нуля», «state machine», «fallback/offline-поведение».
- **Ограничение:** не заявлять проектирование приложения целиком – в интервью описаны фичи/модули.

## 6. Remote Config и data-driven UI

- **Что есть:** контент чипов управляется через Remote Config, JSON → валидация → доменные модели → view states, hardcoded fallback (S10; В26); протоколы с default implementation для карточек Remote Config (В10).
- **Закрывает:** «Remote Config», «feature flags», «data-driven UI», «контент без релиза».
- **Ограничение:** не утверждать, что так устроен весь продукт – только модуль промо-чипов.

## 7. Навигация, deep links, SSO

- **Что есть:** Coordinator/Flow Controller, сброс и перезапуск флоу, 20–30 deep links с программным построением пути (S14; В21); SSO через WebView, Access/Refresh в Keychain, обновление сессии на холодном старте, смена root view.
- **Закрывает:** «навигация», «deep links», «SSO», «Keychain», «восстановление сессии».
- **Ограничение:** universal links и state restoration в интервью не описаны.

## 8. Accessibility и локализация

- **Что есть:** 3–8 европейских языков, `.strings`/`.stringsdict` → String Catalogs, ревизия строк и нейминг ключей; Dynamic Type с кастомными шрифтами; VoiceOver-атрибуты; PR-чек-лист (S11; В22).
- **Закрывает:** «локализация», «Dynamic Type», «VoiceOver», «accessibility».
- **Ограничение:** RTL-опыта нет – не заявлять.

## 9. Медиа и AVFoundation

- **Что есть:** Trim View с лентой кадров, кастомными ползунками и жестами; оптимизация отрисовки (S9; В18); видеоредактор и плеер (master-cv, Stream Vision 2).
- **Закрывает:** «AVFoundation», «видеоредактор», «кастомные UIKit-компоненты», «производительность скролла».
- **Ограничение:** без цифр по производительности – их нет.

## 10. Кросс-платформенная синхронизация решений

- **Что есть:** Mock API синхронизирован с Android-разработчиками (S1; В4); на последнем проекте решение сначала дизайнилось вместе с Android-разработчиком, затем утверждалось у лида/PO (В3, 40).
- **Закрывает:** «кросс-функциональная коммуникация», «консистентность iOS/Android», «согласование архитектуры».
- **Ограничение:** не заявлять владение Android-стеком.

## 11. Продуктовое мышление

- **Что есть:** предложил виджет/Siri/Shortcuts (S2; В5); предложил Demo Mode-архитектуру и получил карт-бланш, аргументировав пользу для бизнеса (S1; В4, 74); предлагал улучшения продукта заказчику (В2, 33); Mega Chips как инструмент монетизации (S10; В26).
- **Закрывает:** «product thinking», «инициатива», «работа с бизнесом».
- **Ограничение:** не приписывать владение продуктовой стратегией.

## 12. AI-assisted development / AI-SDLC

- **Что есть:** более года осознанной практики spec-first, decision-first AI-SDLC на коммерческом iOS-продукте (NDA2) и в пет-проекте (S33; В62). Контракт до кода – SPEC.md и PLAN.md с human approval; lifecycle из 7 фаз (Research → Plan → Execute → Quality Automation → Validate → Merge/Deploy/Telemetry → Refine); границы агента (код/коммит/пуш/PR/review) и человека (merge, approve, release tag, deploy, quality gate, scope); evidence before done по каждому acceptance criterion; tool-neutral harness в Git с адаптерами Cursor / Claude Code / Codex; multi-agent orchestration с lead и ролями research / implementation / review; context & token engineering (AGENTS.md ~9 КБ → ~2,4 КБ, core trio на 42%); feedback loop через memory / ADR / skills. Ранее: Cursor на последнем проекте, фокус на промптах и контроле результата, декомпозиция под AI-процесс (В3, 41–47); AI и скрипты для генерации шаблонов SPM-модулей (S13; В24).
- **Закрывает:** «AI-assisted development», «AI-SDLC», «spec-driven development», «decision-first», «context engineering», «token engineering», «agent governance», «human-in-the-loop», «evidence-based validation», «multi-agent orchestration», «AI code review», «Cursor», «Claude Code», «Codex», «AGENTS.md», «memory / ADR / skills», «ускорение рутины».
- **Ограничение:** не заявлять AI-инфраструктуру компании – это личный рабочий процесс. Не приписывать количественное ускорение: цифр в источнике нет. Практика подтверждена на коммерческом продукте и пет-проекте, но не как формальная роль AI-lead.

## 13. Техдолг и релизные компромиссы

- **Что есть:** осознанное дублирование координатора ради релиза виджета, закрытие через ~1,5 года при модуляризации, спроектированный optimistic behavior (S3; В6).
- **Закрывает:** «tech debt management», «pragmatic trade-offs», «эволюция архитектуры».
- **Ограничение:** optimistic behavior – дизайн, не внедрение.

## 14. Менторство, обучение и публичные выступления

- **Что есть:** `master-cv` – тренер внутреннего учебного центра, ревью кода и менторство студентов, технический интервьюер, серия митапов (XCTest → Swift Testing, Mock-слой для нетворкинга). Интервью добавляет: демо для аудитории 100+ человек (В2, 29); митап про Swift 5.0 и ABI stability в Orangesoft (В7, 110); reskilling коллеги из QA до Junior (В48); программа обучения Orangesoft – 3 студента, 2 трудоустроены (В48); интервью Middle/Senior с live coding и system design (В49); воркшоп по Swift Testing и два митапа по Mock API (В51).
- **Закрывает:** «mentoring», «knowledge sharing», «публичные выступления», «tech talks», «reskilling», «технические интервью».
- **Ограничение:** не добавлять детали, которых нет в CV или интервью (например, конкретные метрики обучения, кроме 3 студентов и 2 трудоустроенных).

## 15. Архитектурные паттерны

- **Что есть:** VIPER на проекте Стрелковый Союз (роутеры, строгое разделение слоёв); MVVM + Coordinator в Stream Vision; MVC на legacy-проектах с постепенным переходом новых фич на MVVM; MVVM → Clean Architecture на последнем проекте (В21, В23).
- **Закрывает:** «VIPER», «MVVM», «MVVM-C», «Clean Architecture», «legacy MVC».
- **Ограничение:** не заявлять TCA/Redux – в интервью их нет.

## 16. Протоколы, generics, обработка ошибок

- **Что есть:** протокол `Toastable` с default implementation (NDA2); протоколы для карточек Firebase Remote Config (NDA1); generic-метод загрузки моков `T: Decodable`; `any`/`some`, associated types; `NetworkError`/`CloudError`, маппинг в UI, `LocalizedError`, централизованный перехват `unlogin` (В10, В11).
- **Закрывает:** «protocol-oriented», «generics», «associated types», «existentials», «typed errors», «error mapping».
- **Ограничение:** не заявлять собственные property wrappers / macros / opaque types – только использование существующих (В7).

## 17. Swift: value/reference и KeyPath

- **Что есть:** осознанный выбор class для иерархии `BaseUser` (Demo/Testing/Mock/Production) и enum со статическими методами для stateless Data Coordinator; KeyPath в SwiftUI, Core Data (`NSSortDescriptor`, `NSFetchRequest`) и Combine (`.assign(to:on:)`) (В9, В13).
- **Закрывает:** «struct vs class», «value semantics», «KeyPath», «Core Data».
- **Ограничение:** не заявлять `@dynamicMemberLookup` и unsafe/C-interop в коммерческих проектах – их не было.

## 18. Фоновые задачи

- **Что есть:** ответ «Мало опыта» (В17) – конкретных внедрений Background Tasks, BGProcessingTask, background upload/download, push-driven wake-up в интервью нет.
- **Закрывает:** ничего.
- **Ограничение:** не заявлять фоновые задачи. Background-приоритет для аналитики и логов (В16) – это приоритет задачи в Swift Concurrency, а не Background Tasks; не путать.

## 19. SwiftUI и state management

- **Что есть:** SwiftUI в продакшене с iOS 14/15; миграция целого модуля UIKit → SwiftUI на NDA2 (экраны профиля и настроек, динамические списки с пагинацией, формы и текстовые поля, графики, кастомные контролы); после перевода последнего UIKit-модуля импорты UIKit удалены из проекта; состояние на `@State`/`@Binding`, `ObservableObject` + `@Published` + Combine, `EnvironmentObject`, макрос `@Observable`; MVVM + `NavigationStack`/`NavigationLink`; интероп через `UIViewRepresentable`/`UIViewControllerRepresentable`, `UIActivityViewController` (S15; В19, В20, В27).
- **Закрывает:** «SwiftUI», «state management», «миграция UIKit → SwiftUI», «интероп UIKit ↔ SwiftUI».
- **Ограничение:** интероп с UIKit остался единичным; не заявлять TCA/Redux и `UIHostingController` (SwiftUI → UIKit) – в интервью этого нет (см. `topics/weak-notes.md`).

## 20. UIKit: адаптивность, дизайн-система, списки

- **Что есть:** на NDA1 полный отказ от Storyboards/XIB в пользу вёрстки кодом и участие в дизайн-системе (переиспользуемые лейблы, кнопки, кастомные вью); на Stream Vision 2 – экран управления устройством (портрет/ландшафт через приоритеты констрейнтов и динамические константы), экран настроек на `UISplitViewController` для iPhone и iPad, prefetching и `prepareForReuse`, галерея с динамической сеткой 3–5 колонок (S16; В18; привязка экранов к проекту подтверждена пользователем).
- **Закрывает:** «UIKit», «Auto Layout», «адаптивность iPhone/iPad», «дизайн-система», «производительность списков».
- **Ограничение:** не заявлять SwiftUI-аналоги этих экранов и транзишены/анимации, которых в интервью нет.

## 21. Сетевой слой

- **Что есть:** нативная обёртка над URLSession на NDA1/NDA2; Alamofire и Moya на Stream Vision и других проектах Orangesoft; token refresh с очередью запросов и автоматическим повтором после 401; токены в Keychain за протоколом хранилища; async/await для сетевых вызовов и отмена через `Task` при уходе с экрана; пагинация Offset/Limit и Cursor-based; типизированные ошибки (S23; В28).
- **Закрывает:** «URLSession», «Alamofire», «Moya», «token refresh», «interceptors», «пагинация», «отмена запросов», «типизированные ошибки».
- **Ограничение:** certificate pinning в интервью не заявлен – не добавлять. Retry-политику отдельно не описывал.

## 22. Хранение данных и миграции

- **Что есть:** Keychain как основное хранилище на NDA2 (токены, Favorite Devices) с `kSecAttrAccessibleWhenUnlocked`; UserDefaults для флагов; FileManager для PDF-чеков MobiScan и кэша аватарок; Core Data через CoreStore на Stream Vision 2; Realm на MobiScan и Merry Kitchen; ручная миграция структуры в Keychain (массив → словарь); lightweight-миграции Core Data и Realm (S24; В29).
- **Закрывает:** «Keychain», «UserDefaults», «FileManager», «Core Data», «CoreStore», «Realm», «миграции схемы».
- **Ограничение:** SwiftData – только план, не внедрение; SQLite/GRDB в интервью нет.

## 23. Offline-first и синхронизация

- **Что есть:** кэш последних данных при входе на экран, skeleton/shimmer вместо блокирующих спиннеров, информативная заглушка без сети; iPhone как единственный источник истины для Apple Watch, обновление состояния при восстановлении связи; отказ от скрытых очередей в пользу явного Toast; NWPathMonitor (S25; В30).
- **Закрывает:** «offline-first», «кэширование», «синхронизация устройств», «Watch Connectivity», «разрешение конфликтов».
- **Ограничение:** сложных merge-стратегий (last-write-wins, версионирование) не было – не заявлять.

## 24. Реактивность

- **Что есть:** Combine как основной инструмент на NDA2 и Stream Vision 2; полная миграция Stream Vision 2 с RxSwift на Combine; debounce для поиска; `@Published` во ViewModel; глобальные подписки на профиль и состояние сети; внедрение `@Observable` и нюансы с `@Bindable`, `environment(object)`, `withObservationTracking` (В31).
- **Закрывает:** «Combine», «RxSwift», «debounce», «data binding», «Observation».
- **Ограничение:** AsyncSequence в продакшене не заявлен; не приписывать сложные операторные цепочки RxSwift.

## 25. CI/CD

- **Что есть:** Bitrise с нуля на Stream Vision 2 (сборка, тесты, TestFlight, уведомления в Telegram); участие в миграции Azure DevOps → GitHub Actions на NDA1/NDA2; quality gates (unit- и snapshot-тесты, SwiftLint, SonarQube, проверки безопасности); автоинкремент номера сборки; TestFlight и Firebase App Distribution (S21; В33).
- **Закрывает:** «CI/CD», «Bitrise», «GitHub Actions», «Azure DevOps», «TestFlight», «quality gates», «версионирование сборок».
- **Ограничение:** сертификатами на крупных проектах управлял заказчик; Xcode Cloud – только изучает в пет-проекте; fastlane в интервью нет.

## 26. Качество кода

- **Что есть:** SwiftLint с нуля на Stream Vision 2; восстановление SwiftLint на NDA2 после нескольких тысяч предупреждений (`swiftlint --fix`, AI-скрипты, ручное ревью); блокировка сборки и мержа по критическим нарушениям и лимиту варнингов; SonarQube с quality gates по покрытию и дублированию; культура ревью с чек-листом, `[weak self]`, retain cycles, Zero Warnings (S22; В34, В46).
- **Закрывает:** «SwiftLint», «SonarQube», «code review», «quality gates», «статический анализ», «code style».
- **Ограничение:** SwiftFormat в интервью не упоминается; не заявлять настройку SonarQube с нуля – только работа с отчётами.

## 27. App Store и релизный процесс

- **Что есть:** ATT на Stream Vision 2 и в пет-проектах, Privacy Manifests только в пет-проекте; прохождение отказов App Review по метаданным и политикам конфиденциальности; IAP-подписки с receipt validation и Restore Purchases на WineBeMine; двухнедельный цикл с Phased Release (1–5%) и hotfix + backmerge на NDA1; TestFlight; Crash-free 99%+ на NDA2 (S27; В35).
- **Закрывает:** «App Store», «App Review», «IAP», «подписки», «phased release», «hotfix», «Privacy Manifest», «ATT», «TestFlight».
- **Ограничение:** Privacy Manifests заявлять только как пет-проект (подтверждено 2026-11-02); на Stream Vision 2 и других коммерческих проектах их не внедрял. Не выдумывать цифры по отказам App Review.

## 28. Производительность и диагностика

- **Что есть:** Instruments (Time Profiler, Network, Leaks, Allocations); Xcode Memory Graph; аудит памяти на NDA2 с выявлением и устранением retain cycles в замыканиях и делегатах; Firebase Crashlytics и Xcode Organizer, приоритизация по охвату, гипотезы по логам (В36, В37).
- **Закрывает:** «Instruments», «утечки памяти», «retain cycles», «Crashlytics», «разбор крашей», «профилирование».
- **Ограничение:** метрик «до/после» в интервью нет; Energy и Animation Hitches не заявлены.

## 29. Холодный старт и размер бандла

- **Что есть:** перевод последовательной инициализации в координаторе на Dispatch Groups на NDA2; очистка Stream Vision 2 от dead code и неиспользуемых ресурсов, аудит ассетов, оптимизация размера бандла, эксперименты со временем сборки (S26; В38, В61).
- **Закрывает:** «launch time», «холодный старт», «размер бандла», «dead code», «build time».
- **Ограничение:** App Thinning и ленивую загрузку целенаправленно не заявлять; конкретных цифр нет.

## 30. Безопасность

- **Что есть:** KeychainSwift и атрибуты доступа; Face ID/Touch ID через LocalAuthentication на NDA1; обфускация перед релизом и динамические ключи с проверкой на бэкенде; временное зашифрованное логирование токенов на NDA2 с удалением из релиза; базовые знания jailbreak-проверок (S28; В39).
- **Закрывает:** «security», «Keychain», «биометрия», «LocalAuthentication», «обфускация», «защита приложения».
- **Ограничение:** certificate pinning не заявлен; jailbreak detection – только теория, не внедрение; шифрование локальной БД не описано.

## 31. Продуктовые решения и UX

- **Что есть:** самостоятельное проектирование UX-флоу QR-сканера на NDA2 с синхронизацией с Android; Quick Actions на Stream Vision 2; предложение Split View; технический контроль дизайн-системы и миграций на NDA1; участие в Bug Bash (В40).
- **Закрывает:** «product thinking», «UX», «инициатива», «работа с дизайнерами», «Bug Bash».
- **Ограничение:** не заявлять владение продуктовой стратегией или A/B-экспериментами – их не было.

## 32. Нечёткие требования и scope creep

- **Что есть:** подготовка edge cases до refinement; 2–3 варианта решения с оценкой сложности; Visitor Management ~год при меняющихся требованиях и зависимости от Web-команды; синхронизация с Android/Web и назначение ответственного за уточнения; фиксация договорённостей в Jira и Confluence; прототип при отсутствии требований (S18; В41).
- **Закрывает:** «scope creep», «unclear requirements», «trade-offs», «работа с BA», «документирование решений».
- **Ограничение:** не заявлять формальную роль продукт-оунера.

## 33. Защита технических инициатив

- **Что есть:** аргументация через Time-to-Market и рост стоимости следующих фич (Stream Vision 2); постепенное внедрение дизайн-системы вместо «месяца на перекрашивание» (NDA1); Quick Actions в свободное время с последующим включением в релиз; восстановление SwiftLint через ускорение ревью и спринта (NDA2); Boy Scout Rule как компромисс (В42).
- **Закрывает:** «stakeholder management», «защита рефакторинга», «техдолг», «аргументация через риски».
- **Ограничение:** не приписывать формальную бюджетную ответственность.

## 34. Оценка задач

- **Что есть:** Story Points по Фибоначчи, 3 SP ≈ 1 день; Planning Poker; декомпозиция задач выше 5–8 SP; Spike-тикеты; не брать задачу в спринт без согласованных контрактов API; тесты и аналитика в оценке по умолчанию; раннее оповещение о рисках; небольшой буфер (В43).
- **Закрывает:** «estimation», «story points», «planning poker», «spike», «декомпозиция», «управление рисками».
- **Ограничение:** не заявлять t-shirt sizing и SAFe.

## 35. Инциденты в продакшене

- **Что есть:** краши мега-чипов после релиза на NDA1; обнаружение через Crashlytics, тикет и тред в Slack, информирование стейкхолдеров; отключение фичи через Feature Flag на бэкенде до хотфикса; замена нестабильной сторонней библиотеки на нативный подход; post-mortem, обязательность Feature Flags, аудит зависимостей и unit-тесты на переключение состояний (S19; В44).
- **Закрывает:** «incident management», «feature flags», «post-mortem», «мониторинг», «hotfix».
- **Ограничение:** Crash-free в этом кейсе оставался 95–98% – не путать с общим 99%+ на NDA2.

## 36. Agile и Definition of Done

- **Что есть:** refinement, planning, daily, demo, retro; дейли ежедневно на NDA1 и через день на NDA2; демо 100+ на английском; участие в Design Review iOS-команды (~20–30 инженеров); DoD из шести пунктов: требования, качество кода и ревью, unit-тесты, аналитика, локализация, CI (В45).
- **Закрывает:** «Agile», «Scrum», «DoD», «demo», «retro», «refinement».
- **Ограничение:** Kanban, SAFe и формальную роль Product Owner не заявлять.

## 37. Scrum Master и улучшение процесса

- **Что есть:** недельная ротация роли Scrum-мастера на NDA2 с ведением Daily и фиксацией блокеров; внедрение чек-листа для Pull Request; дробление крупных PR на атомарные части; SwiftLint как снижение шума на ревью; автоматические проверки в DoD (S22; В46).
- **Закрывает:** «facilitation», «Scrum Master», «code review process», «process improvement».
- **Ограничение:** это ротация, а не постоянная должность – формулировать как участие.

## 38. Управление техдолгом

- **Что есть:** процент ёмкости спринта на техдолг на NDA1, аргументация через тимлида и PO; использование периодов затишья бизнеса для рефакторинга; TODO с дублированием в Jira; Boy Scout Rule; инициированное обсуждение перехода на новые Swift/Xcode на Stream Vision 2 (В47).
- **Закрывает:** «tech debt», «capacity planning», «refactoring strategy», «обновление технологий».
- **Ограничение:** конкретный процент ёмкости в интервью не назван – не выдумывать.

## 39. Менторство и найм

- **Что есть:** тренер в ISsoft, reskilling коллеги из QA до Junior (работает в штате); программа обучения Orangesoft с нуля, 3 студента, 2 трудоустроены; code review и pair programming как обучение; интервью Middle/Senior с технической секцией, live coding и system design, письменный фидбек и синхронизация со вторым интервьюером; онбординг junior на Stream Vision 2 (S29; В48, В49, В54).
- **Закрывает:** «mentoring», «reskilling», «hiring», «interviewing», «onboarding».
- **Ограничение:** не заявлять формальную позицию Team Lead или Head of iOS.

## 40. Техническое лидерство и knowledge sharing

- **Что есть:** Mock API как investigation со сравнительным анализом и защитой решения; Design Review с солюшн-архитекторами на NDA1; feature ownership Visitor Management с декомпозицией, распределением задач и контролем кода коллеги; разруливание блокеров с Backend/Design и эскалация; общие протоколы и базовые классы как стандарт команды; воркшоп Swift Testing, два митапа по Mock API, обмен опытом по AI-инструментам (S30, S31; В50, В51).
- **Закрывает:** «technical leadership», «ownership», «design review», «knowledge sharing», «tech talks».
- **Ограничение:** лидерство без формальной должности – не превращать в «руководил командой из N человек».

## 41. Коммуникация с заказчиком, распределённые команды, передача проектов

- **Что есть:** mixed teams с прямым контактом с PO, техлидами, дизайнерами и BA; вся коммуникация на английском; daily, design review, Slack, Jira, Confluence; демо 100+ в Teams; опыт работы через PM на Stream Vision 2; часовые пояса США (Чикаго), Индия, Европа, «золотое окно» и async-first; онбординг в NDA1/NDA2 со схемами зависимостей; knowledge transfer по MobiScan; стабилизация legacy Realt (realt.by) при рассинхронизации бэкендов; английский B2 и 5+ лет англоязычной среды (S32; В52–В54, В60).
- **Закрывает:** «client communication», «English», «distributed team», «async communication», «handover», «legacy intake».
- **Ограничение:** не заявлять C1 и выше; польский – только понимание.

## 42. Аутсорс и продуктовая разработка

- **Что есть:** работа в крупных аутсорс-компаниях, но преимущественно в интегрированных продуктовых командах; ownership и долгосрочное влияние на архитектуру; IoT как драйвер интереса; осознанный переход в продуктовую разработку (В55).
- **Закрывает:** «product mindset», «ownership», «аутсорс-опыт», «мотивация перехода в продукт».
- **Ограничение:** не заявлять, что работал только в продуктовых компаниях.

## 43. Широта стека и смежные платформы

- **Что есть:** SwiftUI, UIKit, Core Animation, Lottie, Charts, AVFoundation/AVKit, Core Image, Vision, CoreLocation, MapKit, Yandex Maps SDK, WidgetKit, CarPlay (code review), Watch Connectivity, SiriKit/App Intents, Combine, RxSwift, Alamofire, Moya, Core Data/Realm, Keychain/UserDefaults, Firebase, StoreKit, APNs, Core Bluetooth, Swift Testing/XCTest, ViewInspector; Charles Proxy с Map Local и breakpoints, Instruments, Bitrise, GitHub Actions/Azure, SwiftLint, SPM, SwiftGen/R.swift; watchOS в продакшене, CarPlay через ревью, macOS-утилиты, Catalyst; KMP и Core ML – пет-проекты; tvOS – теория, visionOS – нет (В56–В58).
- **Закрывает:** «стек iOS», «фреймворки», «инструменты разработчика», «watchOS», «CarPlay», «IoT».
- **Ограничение:** Flutter/React Native – только понимание концепций; App Clips, HealthKit, ARKit и visionOS не заявлять; Core ML и KMP – изучение, не продакшен.
