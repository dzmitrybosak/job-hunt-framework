# Experience insights – производный слой от self-interview

Источник: `profile/self-interview.md` (**только чтение, не изменять**). Здесь компактная навигация и структурированные факты для флоу вакансий.

Обновлено: 2026-11-02 (61 вопрос; расширение 27–61 – сеть, данные, качество, релизы, производительность, безопасность, продукт, процесс, менторство, аутсорс, стек).

Как пользоваться:
1. Открыть этот индекс → найти тему.
2. При нехватке деталей – `grep` по номеру вопроса в `profile/self-interview.md` и точечное чтение строк.
3. Факты брать только из источников; смысл не искажать, менять можно только формулировку (`prompts/_common.md` → «Источники фактов и fact fidelity»).

Обозначения: **NDA1** – Платформа управления недвижимостью и доступом (Октябрь 2021 – февраль 2024), **NDA2** – Платформа управления доступом (Февраль 2024 – Октябрь 2026); в `master-cv` оба проекта идут с пометкой (NDA).

## Карта вопросов

### Часть 1. Профиль, язык, память, архитектура

| № | Тема | Строки | Ключевое |
|---|---|---|---|
| В1 | Хронология: EPAM → Orangesoft → ISsoft | 3–6 | 2018–2026, домены, роли; Orangesoft: новостное MVP, Realt, Merry Kitchen, Mobiscan, Стрелковый Союз, Stream Vision 2 |
| В2 | Переходы и мотивация | 8–35 | legacy, 5+ проектов, кросс-функциональные команды, демо 100+, митапы, AI, продуктовое мышление |
| В3 | Рабочий день / процессы | 37–54 | NDA2: AI + Cursor, 4 iOS (CV), ревью 15 мин–1 ч; NDA1: 5–7 команд, ~20–30 iOS на проекте, 3–4 в команде, дизайн-ревью, демо заказчику |
| В4 | Сложнейший технический вызов: Mock API / Demo Mode | 56–74 | ~1 месяц проектирования, переиспользование сетевого слоя, синхронизация с Android |
| В5 | Главный проект: интерактивный виджет | 77–94 | App Intents, Siri, Shortcuts, 1M+ открытий |
| В6 | Техдолг виджета и его закрытие | 96–107 | дублирование координатора, SPM/Clean через ~1,5 года, optimistic behavior |
| В7 | Версии Swift и эволюция языка | 108–113 | с 4.2, митап Swift 5.0, async/await, actor, generics, Result на Stream Vision 2 |
| В8 | ARC и память | 114–116 | Memory Graph; конкретный кейс не назван (дополняется В36) |
| В9 | Value vs Reference types | 117–135 | BaseUser-иерархия, enum Data Coordinator |
| В10 | Протоколы, generics, existentials | 136–149 | Toastable (NDA2), Remote Config карточки (NDA1), generic mock loader, BaseViewController<State>, any/some |
| В11 | Error handling | 151–178 | NetworkError/CloudError, маппинг в UI, LocalizedError, централизованный unlogin |
| В12 | Objective-C и bridging | 180–191 | миграция .h/.m → Swift, Bridging Header, @objc, KVC как крайняя мера |
| В13 | Метапрограммирование и unsafe API | 192–203 | KeyPath (SwiftUI, Core Data, Combine); unsafe/C-interop в коммерции не было |
| В14 | GCD/Operations → Swift Concurrency | 204–223 | withCheckedContinuation, OperationQueue, отмена, actor, TaskGroup |
| В15 | Actors, @MainActor, Sendable | 224–238 | Sendable-модели, Transition-модели, actor в Mock API, семафоры на Stream Vision |
| В16 | Структурированная конкурентность | 239–245 | TaskGroup в Launch Coordinator, detached для Siri, приоритеты |
| В17 | Фоновые задачи | 246–250 | **«Мало опыта»** – Background Tasks / BGProcessingTask / background upload не заявлять |
| В18 | UIKit и кастомные компоненты | 251–260 | Trim View, адаптивность (ориентации, Split View), дизайн-система на NDA1, prefetching, галерея 3–5 колонок; экраны управления устройством и настроек – Stream Vision 2 |
| В19 | SwiftUI и state management | 262–277 | iOS 14/15, миграция модуля на NDA2, @State/@Binding, ObservableObject, EnvironmentObject, @Observable |
| В20 | Интероп UIKit ↔ SwiftUI | 279–282 | UIViewRepresentable / UIViewControllerRepresentable, UIActivityViewController |
| В21 | Навигация и сложные флоу | 284–304 | VIPER-роутеры, Coordinator, Flow Controller, 20–30 deep links, iPad Split View, SSO |
| В22 | Accessibility и локализация | 306–314 | 3–8 языков, String Catalogs, VoiceOver, Dynamic Type, PR-чек-лист |
| В23 | Архитектурные паттерны | 318–335 | VIPER, MVVM-C, RxSwift → Combine, SPM-модули, Clean Architecture, legacy MVC |
| В24 | Модуляризация | 337–351 | Core/Feature-модули, гибрид SPM + CocoaPods, фича-флаги, рост времени сборки |
| В25 | DI | 353–373 | Swinject, initializer injection, Environment/Dependencies, миграция со статики |
| В26 | System Design: Mega Chips | 375–395 | Remote Config, Data Driven UI, fallback, state machine, Tooltips, Design Review |

### Часть 2. Рефакторинг, сеть, данные, качество, релизы

| № | Тема | Строки | Ключевое |
|---|---|---|---|
| В27 | Рефакторинг и легаси | 397–411 | Boy Scout Rule, аргументация через риски, feature flags и раскатка 5% → 20%, декомпозиция legacy-контроллера; полный уход от импортов UIKit подтверждён (последний модуль переведён на SwiftUI, интероп единичный) |
| В28 | Сетевой слой | 414–430 | URLSession-обёртка на NDA1/NDA2, Alamofire/Moya на Stream Vision, token refresh с очередью, Keychain, async/await, пагинация Offset и Cursor, типизированные ошибки |
| В29 | Хранение данных | 431–448 | Keychain (NDA2, включая Favorite Devices), UserDefaults, FileManager (PDF-чеки MobiScan, кэш аватарок), Core Data/CoreStore (Stream Vision 2), Realm (MobiScan, Merry Kitchen), миграции схемы и Keychain, SwiftData только план |
| В30 | Offline-first | 449–465 | кэш + skeleton/shimmer, заглушка без сети, iPhone как источник истины для Watch, Toast вместо скрытых очередей, NWPathMonitor |
| В31 | Реактивность | 466–480 | Combine как основной, RxSwift → Combine на Stream Vision, debounce для поиска, @Published, @Observable и его нюансы (Bindable, environment(object), withObservationTracking) |
| В32 | Тестирование | 483–499 | аудит и рост 13% → 75% (в В32 ошибочно 17%), мастер-класс XCTest → Swift Testing, ViewInspector, SnapshotTesting, тесты в CI, DI-тестируемость |
| В33 | CI/CD | 500–511 | Bitrise с нуля (Stream Vision) + Telegram, Azure → GitHub Actions (NDA1/NDA2), quality gates, TestFlight и Firebase App Distribution, автоинкремент билда, code signing |
| В34 | Code quality | 512–528 | SwiftLint с нуля (Stream Vision), восстановление SwiftLint и несколько тысяч предупреждений (NDA2), SonarQube, quality gates, культура ревью и менторство |
| В35 | App Store и релизы | 529–542 | ATT (Stream Vision 2 и пет-проекты), Privacy Manifests только в пет-проекте, отказы App Review, IAP с receipt validation и Restore Purchases (WineBeMine), RevenueCat в пет-проекте, Phased Release, hotfix + backmerge, Crash-free 99%+ |
| В36 | Instruments | 545–550 | Time Profiler, Network, Leaks/Allocations; аудит памяти на NDA2, устранение retain cycles в замыканиях и делегатах |
| В37 | Crash reporting | 551–555 | Firebase Crashlytics + Xcode Organizer, приоритизация по охвату, гипотезы по логам, высокий Crash-free |
| В38 | Размер и скорость | 556–559 | холодный старт через Dispatch Groups на NDA2, dead code и ассеты на Stream Vision 2, размер бандла |
| В39 | Безопасность | 562–573 | KeychainSwift и kSecAttrAccessibleWhenUnlocked, Face ID/Touch ID через LocalAuthentication (NDA1), обфускация и динамические ключи (NDA1), отладочное логирование токенов (NDA2, удалено из релиза), базовые знания jailbreak-проверок |

### Часть 3. Продукт, процесс, лидерство

| № | Тема | Строки | Ключевое |
|---|---|---|---|
| В40 | Продуктовые решения | 580–590 | самостоятельный UX-флоу QR-сканера (NDA2), Quick Actions (Stream Vision 2), Split View, восстановление SwiftLint, Bug Bash, технический контроль дизайн-системы (NDA1) |
| В41 | Нечёткие требования и scope creep | 591–605 | edge cases до refinement, 2–3 варианта решения, Visitor Management ~год при меняющихся требованиях, синхронизация с Android/Web, фиксация в Jira/Confluence, прототип при отсутствии требований |
| В42 | Защита технических инициатив | 606–617 | аргументация через Time-to-Market (Stream Vision), постепенное внедрение дизайн-системы (NDA1), Quick Actions в свободное время, SwiftLint и скорость ревью (NDA2), Boy Scout Rule |
| В43 | Оценка задач | 618–633 | Story Points по Фибоначчи (3 SP ≈ 1 день), Planning Poker, декомпозиция > 5–8 SP, Spike-тикеты, контракты API до спринта, раннее оповещение о рисках |
| В44 | Инциденты в продакшене | 634–650 | краши мега-чипов после релиза (NDA1), Feature Flag как немедленный стоп, замена сторонней библиотеки на нативный подход, Post-mortem и аудит зависимостей |
| В45 | Agile | 653–675 | refinement/planning/daily/demo/retro, демо 100+ на английском, Design Review iOS-команды (~20–30), DoD из 6 пунктов |
| В46 | Scrum Master / улучшение процесса | 676–686 | ротация Scrum-мастера (NDA2), чек-лист PR, дробление PR, SwiftLint, CI в DoD |
| В47 | Техдолг | 687–697 | процент ёмкости спринта на NDA1, аргументация через тимлида и PO, TODO + тикеты в Jira, Boy Scout Rule, обновление Swift/Xcode на Stream Vision |
| В48 | Менторство | 700–711 | тренер в ISsoft, reskilling тестировщика до Junior, программа обучения в Orangesoft (3 студента, 2 трудоустроены), код-ревью и pair programming, кросс-платформенное обучение Android/Backend |
| В49 | Технические собеседования | 712–725 | Middle/Senior в ISsoft, техническая секция + live coding + system design, фидбек по форме, синхронизация со вторым интервьюером |
| В50 | Техническое лидерство без должности | 726–738 | Mock API как investigation, Design Review с солюшн-архитекторами, feature ownership Visitor Management, разруливание блокеров, общие протоколы и базовые классы |
| В51 | Тренинги и tech talks | 739–754 | митап по Swift 5.0 (Orangesoft), воркшоп XCTest → Swift Testing, 2 митапа по Mock API, обмен опытом по AI-инструментам, демо 100+ на английском |
| В52 | Коммуникация с заказчиком | 757–775 | mixed teams, английский, daily и design review, Slack, работа с BA, spike-документация, демо 100+ в Teams, опыт работы через PM (Stream Vision) |
| В53 | Распределённая команда | 776–794 | США (Чикаго), Индия, Европа; «золотое окно», async-first, документация в Confluence, Jira, PR |
| В54 | Передача и приемка проектов | 795–817 | онбординг в NDA1/NDA2, схемы зависимостей, handover MobiScan, онбординг junior на Stream Vision, legacy Realt (realt.by) и рассинхронизация бэкендов |
| В55 | Аутсорс vs продукт | 818–830 | интегрированные продуктовые команды, ownership, IoT как драйвер, осознанный переход в продукт |
| В56 | Фреймворки и библиотеки | 835–872 | SwiftUI/UIKit, Core Animation, Lottie, Charts, AVFoundation, Core Image, Vision, MapKit, Yandex Maps, WidgetKit, CarPlay, Watch Connectivity, App Intents, Combine, RxSwift, Alamofire, Core Data/Realm, Firebase, StoreKit, APNs, Core Bluetooth, Swift Testing/XCTest, ViewInspector; KMP и Core ML – пет-проекты |
| В57 | Инструменты разработчика | 873–890 | Charles (Map Local, breakpoints), Instruments, Bitrise, GitHub Actions/Azure, SwiftLint, SPM, Dev/Stage/Prod, SwiftGen/R.swift, Xcode debugger |
| В58 | Смежные платформы | 891–906 | watchOS (NDA1/NDA2), CarPlay (NDA2, code review), KMP – изучение, macOS-утилиты, Catalyst; tvOS – теория, visionOS – нет |
| В59 | Обучение и комьюнити | 907–928 | Hacking with Swift, SwiftLee, WWDC, iOS Dev Weekly, книги, пет-проект AI-помощника, митапы Viber/Т-Банк, Mobius/Podlodka, GitHub (приватные репозитории) |
| В60 | Языки | 929–943 | английский B2, 5+ лет англоязычной среды, переговоры и оценки перед заказчиками; русский, белорусский, польский – понимание |
| В61 | Что не вошло | 944–958 | менторство junior на Stream Vision, гайды по code review, GitFlow, dead code removal и build time, UX-инициативы, Bug Bash, курс «Эффективные переговоры» |

## Файлы слоя

- `stories/star-stories.md` – 32 истории в STAR + короткие версии (для cover letter и сообщений).
- `stories/cv-bullets.md` – пул кандидатов в формате CV: структура master-cv (компания → проект → bullets), без нарратива; плюс подсекция «Внепроектная деятельность» по работодателям. RU подтверждён 2026-11-02, EN – DRAFT (пересобрано 2026-11-02).
- `evidence/evidence-map.md` – цифры и масштабы: где подтверждены.
- `gaps/bridges.md` – опыт из интервью, не выведенный в резюме, и какие гэпы он закрывает.
- `topics/weak-notes.md` – пустые/слабые ответы и расхождения с CV.
