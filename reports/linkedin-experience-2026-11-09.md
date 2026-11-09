# LinkedIn Experience: разбор и варианты улучшения

Дата: 2026-11-09. Вход: `score.md` (Experience 5/10), текущие описания Orangesoft и ISsoft, `profile/master-cv-en.md`, `profile/achievements.md`, `profile/experience-insights/` (cv-bullets, evidence-map), `profile/positioning.md`, `profile/target-role.md`.

Цель: Experience ≥ 8/10. Язык профиля – английский, поэтому все тексты для вставки на английском; анализ на русском.

---

## 1. Почему сейчас 5/10

Скоринг усредняет оценки по каждой записи об опыте. Проверки из `score.md` и то, как их проходят текущие описания:

| # | Проверка | Сейчас | Комментарий |
|---|---|---|---|
| 1 | Hard skills в job title | ✗ | Обе записи – «iOS Developer», ни одного навыка |
| 2 | Конкретный title | ✗ | «iOS Developer» помечен как vague; в CV при этом «Senior iOS Developer» |
| 3 | Детали описания | ~ | Достижения есть, но структура сломана: буллеты склеены в одну строку, у проектов нет дат, у первого проекта нет масштаба |
| 4 | Red flags / безработица | ? | Даты ISsoft «Present» расходятся с CV (октябрь 2026); 2019–2021 без чисел выглядит слабее |
| 5 | Quantified impact | ~ | Coherent – да (1M+, 160K+, 99.8%, 13→75%); Orangesoft – ни одной цифры |
| 6 | Weak language | ~ | «Worked on», «Contributed to», «Developed key product UI» |
| 7 | Spelling | ✓ | Ошибок нет |
| 8 | Active voice | ~ | Часть буллетов пассивна/безлична |
| 9 | Special characters | ✗ | Названия проектов начинаются с «–», буллеты «•» стоят в середине строки |
| 10 | Buzzwords | ✓ | Клише нет |

Главный вывод: проблема не в фактуре (достижения сильные), а в **упаковке и ключевых словах**. Скоринг считает среднее по записям – значит выгодно, чтобы каждая запись была самодостаточной: title с навыками, проект с датами, метрики в первых строках, стек отдельной строкой.

---

## 2. Три варианта

| | Что делаем | Прогноз | Время | Риск |
|---|---|---|---|---|
| **A. Косметика** | Меняем только title + чиним переносы строк и ведущие «–» | **7/10** | 15 мин | Не хватает на цель: описания остаются без чисел (Orangesoft) и без структуры |
| **B. Структурный рерайт (рекомендую)** | Title с навыками + рерайт описаний: проект → даты → метрики в первых строках → стек; всё в лимите 2000 символов | **8.5/10** | 40 мин | Нужно вставить текст целиком, а не править по кускам |
| **C. B + разбивка на 4 позиции** | В каждой компании – две отдельные записи (по проекту) со своим title и навыками | **9/10** | 60 мин | Две записи с одинаковым title в одной компании; при экспорте в PDF выглядит как две роли |

Прогноз – оценка по 10 проверкам из `score.md`, а не гарантия алгоритма. B закрывает 9 из 10 проверок; C добавляет попадание в поиск по двум разным наборам навыков (SwiftUI/WidgetKit и UIKit/AVFoundation) и поднимает среднее, потому что каждая запись оптимизирована отдельно.

---

## 3. Вариант B – готовый текст

### 3.1. Job title (поле Title)

- Coherent Solutions / ISsoft: `Senior iOS Developer | Swift, SwiftUI, UIKit, Modular Architecture`
- Orangesoft: `iOS Developer | Swift, UIKit, AVFoundation, Video Streaming`

Правило: title = реальная должность + 2–4 навыка через запятую. Не превращать в слоган и не добавлять навыков, которых не было.

### 3.2. ISsoft – описание (1996 символов, лимит 2000)

```
Senior iOS engineer on two access platforms (160K+ and 500K+ DAU), owning device control and Apple integrations.

Access Management Platform (NDA) | Feb 2024 – Oct 2026
• Built interactive device management widgets that reached 1M+ user interactions on a product serving 160K+ daily active users, contributing to a 99.8% crash-free rate.
• Raised unit test coverage from 13% to 75%: audited coverage by layer, adopted Swift Testing as the team standard and added snapshot tests.
• Contributed to a feature-based modular architecture (SPM, MVVM, Clean Architecture) that reduced coupling between features.
• Migrated a module from UIKit to SwiftUI, part of a migration that ended with all UIKit imports removed from the project.
• Built Apple ecosystem integrations: Widgets with Siri and Shortcuts, App Intents, and Apple Watch sync with iPhone as the single source of truth.
• Implemented SSO with Keychain tokens, token refresh with a request queue and adaptive iPad navigation.
• Ran a spec-first, AI-assisted SDLC for over a year: human-approved SPEC.md and PLAN.md, a seven-phase lifecycle and evidence for every acceptance criterion.
Technologies: Swift, SwiftUI, Combine, App Intents, WidgetKit, WatchConnectivity, CarPlay, Firebase, SPM

Property & Access Management Platform (NDA) | Oct 2021 – Feb 2024
• Developed business-critical features for an app serving 500K+ daily active users: guest passes, access permissions, scheduled actions and notifications.
• Designed client-side synchronization between apps, accounts and backend APIs to keep state consistent across complex flows.
• Built Mega Chips, a data-driven Home Screen component with Remote Config and fallback states; presented it at a Design Review for 20 developers.
• Supported 20–30 deep link scenarios and long device-connection flows with a Flow Controller.
• Moved the UI from Storyboards to code-based layout and contributed to the design system.
Technologies: Swift, UIKit, Combine, AVFoundation, Firebase, Core Data
```

### 3.3. Orangesoft – описание (1794 символа)

```
Built Stream Vision 2, an IoT app for digital night vision and thermal imaging devices: live video from the device, media editing, cloud storage and a news feed. Shipped to the App Store and supported after launch; the app is rated 4.7/5 across 1.2K ratings.

Stream Vision 2 | Nov 2019 – Oct 2021
• Built the complete UI for core flows across multiple design iterations: live viewfinder, gallery, video editor with trimming and export, device management and settings.
• Implemented real-time device interaction and video streaming over UDP sockets, turning the iPhone into a viewfinder and control interface for connected devices.
• Built the Trim View video editor from scratch: frame thumbnails, custom range sliders and gesture handling, with smooth scrolling on the frame strip.
• Implemented a cloud upload and download queue on OperationQueue with dependencies, bounded concurrency and cancellation of stale tasks.
• Built a dynamic 3–5 column gallery grid with prefetching and cell reuse, and adapted device control and settings screens for portrait, landscape and iPad Split View.
• Migrated the project from RxSwift to Combine, removing a third-party dependency while keeping 100% of functionality.
• Reduced build times, optimized cloud uploads and refactored components; removed dead code and unused assets and cut the bundle size.
• Owned Bitrise CI (build, tests, TestFlight, notifications), set up SwiftLint and introduced the first systematic unit tests on the project.
Technologies: Swift, UIKit, AVFoundation, Combine, Core Data, CoreStore, Firebase, CocoaAsyncSocket, Swinject

Other projects: retail barcode scanning with an electronic cart, a real estate platform, a wine selection and table booking app with subscriptions, a sports calendar, and a culinary social network.
```

### 3.4. Skills к каждой позиции (до 5)

- ISsoft: Swift, SwiftUI, UIKit, Combine, Unit Testing
- Orangesoft: Swift, UIKit, AVFoundation, Core Data, CI/CD

### 3.5. Что изменилось по сравнению с текущим

- В первых двух строках – масштаб продукта (до свёртки «see more»).
- У проектов появились даты и отдельная строка технологий.
- Метрики подняты в начало буллетов (1M+, 160K+, 99.8%, 13→75%, 500K+, 4.7/5).
- Глаголы в активном залоге, прошедшее время: Built, Raised, Designed, Migrated, Ran, Owned.
- Убраны: склейка буллетов, ведущий «–» в названиях проектов, «Worked on», «Contributed to» в качестве ведущего глагола.
- Добавлены факты, которые были в CV, но не в LinkedIn: RxSwift → Combine, Bitrise и SwiftLint с нуля, первые unit-тесты, iPad Split View, phased rollout, CI-миграция, Design Review на 20 разработчиков.

---

## 4. Вариант C – разбивка на 4 позиции

В LinkedIn у одной компании можно вести несколько позиций – они группируются под компанией и суммируют стаж. Это самый прямой способ поднять **среднее**: скоринг считает каждую запись отдельно, и каждая получает свой title с навыками, свои даты и свой набор skills.

| Компания | Title | Даты | Описание |
|---|---|---|---|
| ISsoft | Senior iOS Developer \| SwiftUI, WidgetKit, App Intents | Feb 2024 – Oct 2026 | блок Access Management из B (пункт 3.2, до строки Technologies) |
| ISsoft | Senior iOS Developer \| UIKit, Combine, AVFoundation | Oct 2021 – Feb 2024 | блок Property & Access из B |
| Orangesoft | iOS Developer \| Swift, AVFoundation, Video Streaming | Nov 2019 – Oct 2021 | блок Stream Vision 2 из B |
| Orangesoft | iOS Developer \| Swift, UIKit, StoreKit, Maps | Jan 2019 – Nov 2019 | строка Other projects + 3–4 буллета из `cv-bullets.md` (MobiScan, WineBeMine, Realt) |

Оговорки:
- Title в обеих записях ISsoft – «Senior iOS Developer»: уровень не менялся, поэтому создавать видимость повышения нельзя; различаются только ключевые слова.
- Четвёртая позиция (январь–ноябрь 2019) – реальный период других проектов; если не хочется плодить записи, оставить три.
- Если в компании есть политика одной записи на работодателя или профиль часто выгружают в PDF для ATS, вариант B безопаснее.

---

## 5. Механика, которая добавляет баллы помимо текста

1. **Даты.** В LinkedIn ISsoft стоит «October 2021 – Present», в CV – октябрь 2026. Привести к одному факту: либо `Present`, либо `Oct 2026`. Расхождение с резюме – кандидат в red flag.
2. **Локация.** `Brest, Belarus` → `Belarus (Remote)` у текущей/последней роли: совпадает с target-role (только удалёнка) и попадает в фильтры рекрутеров.
3. **Media.** К Orangesoft прикрепить ссылку на Stream Vision 2 в App Store; к ISsoft – скриншот архитектурной схемы без NDA-деталей (или ничего, если нельзя).
4. **Рекомендации.** 2–3 рекомендации от коллег/лида – не влияют на Experience напрямую, но поднимают доверие к цифрам.
5. **Компания.** Сейчас выбрана страница ISsoft. Если важнее поиск по бренду Coherent Solutions, выбрать её страницу, а в первой строке описания написать «ISsoft, a Coherent Solutions company». Оба варианта допустимы, выбирать по тому, по какому имени вас ищут.
6. **Дубли в Skills.** Навыки из описаний должны быть в разделе Skills профиля – иначе алгоритм не связывает текст с навыками.

---

## 6. Fact fidelity – что проверено и что нельзя добавлять

Все цифры в текстах B взяты из `achievements.md` / `master-cv-en.md` / `experience-insights`:
1M+ взаимодействий и 160K+ DAU, 99.8% crash-free, 13→75% покрытия, 500K+ DAU, Design Review 20 разработчиков, 2 недели цикл и 1–5% раскатки, 4.7/5 и 1.2K оценок, 100% функциональности после RxSwift → Combine.

Не добавлять (нет в источниках или цифра не подтверждена):
- проценты ускорения сборки, сокращения крашей, роста ретеншена;
- «led a team», «owned the roadmap» – роль в источниках другая;
- любые цифры по Orangesoft, кроме рейтинга App Store и состава команды (2 iOS-инженера);
- «reduced build times by X%» – в источнике только факт снижения.

Осознанно опущено из-за лимита 2000 символов: cold start через TaskGroup, offline-состояния, Guest Passes как отдельный буллет, biометрия и обфускация, SonarQube. Эти факты остаются в CV; при желании менять местами с текущими буллетами, но не выходить за лимит.
