# Gap analysis – Детмир Тех («Детский мир») / iOS-разработчик

- Режим: A (по JD)
- Дата: 2026-10-23
- Ссылка: – (paste)

## Match: 90% – strong fit

Расчёт: must 1.0 × 0.7 + nice 0.6875 × 0.3 = 0.7 + 0.206 = 0.906 → **90%** (округление вниз, консервативно)

Ядро JD покрывается напрямую: 7+ лет коммерческой iOS-разработки, SwiftUI и UIKit в продакшене, Swift Concurrency, модульная архитектура на SPM, тестируемость (13% → 75%), code review. После обновления CV закрылся и RxSwift: миграция целого проекта с RxSwift на нативный Combine с сохранением 100% функциональности – обе стороны будущей миграции RxSwift → AsyncStream знакомы на практике. Остаются «инфраструктурные» плюсы (Tuist, GitLab CI/CD, Fastlane, SnapshotTesting) – закрываются смежным реальным опытом (модульность на SPM; CI/CD на Azure DevOps/Bitrise/GitHub Actions) и честной готовностью быстро подтянуть. Опасность не техническая, а организационная: ТК РФ и вилка (агрегаторная медиана ~217–258K ₽ заметно ниже целевых 4500 USD).

## Must-have

| Требование | Статус | Что из CV использовать |
|---|---|---|
| Опыт коммерческой iOS-разработки от 3 лет | ✅ full | 7+ лет: Orangesoft (01/2019–10/2021), Coherent Solutions Senior iOS (10/2021 – настоящ. время) |
| Уверенное знание Swift | ✅ full | Swift – основной язык 7+ лет во всех проектах, включая pet-проект Between на SwiftUI + Swift Concurrency |
| Практический опыт со SwiftUI и UIKit | ✅ full | SwiftUI в продакшене (Access Management Platform, Between) + продолжающаяся миграция UIKit → SwiftUI; UIKit – 500K+ DAU проект и Stream Vision 2 |
| Понимание Swift Concurrency и управления асинхронными операциями | ✅ full | Swift Concurrency (async/await) в стеке текущего проекта и Between; распределённые backend-системы и real-time сценарии |
| Опыт работы с RxSwift | ✅ full | Stream Vision 2: миграция проекта с RxSwift на нативный Combine с сохранением 100% функциональности и отказом от сторонней зависимости; миграция UIKit → SwiftUI – типовой опыт миграции реактивных слоёв |
| ООП, ФП и архитектура мобильных приложений | ✅ full | MVVM, Clean Architecture, Feature-Based Modularization (SPM); проектирование модулей и API |
| Клиент-серверные приложения и REST API | ✅ full | Интеграции распределённых backend-сервисов, client-backend state sync, REST APIs; Moya/Alamofire в прошлом проекте |
| Поддерживаемый и тестируемый код | ✅ full | Покрытие unit-тестами 13% → 75% (XCTest, Swift Testing, ViewInspector), spec-driven AI-SDLC с циклом валидации |
| Уверенное владение Git | ✅ full | Git во всех проектах, PR review как часть CI-цикла |
| Английский для чтения технической документации | ✅ full | B2 (Upper-Intermediate); все проекты с английскими доками и коммуникацией |

**score_must = 10 × 1.0 / 10 = 1.0**

## Nice-to-have

| Требование | Статус | Комментарий |
|---|---|---|
| Крупные модульные приложения | ✅ full | Feature-based модульная архитектура на SPM (MVVM, Clean, явные границы feature-модулей); у них ~90 SPM-пакетов, тест на масштаб – прямое совпадение |
| Постепенная миграция legacy-кода | ✅ full | Постепенная миграция UIKit → SwiftUI в текущем проекте 4+ года; рефакторинг legacy-компонентов в 500K+ DAU проекте |
| Знание SPM и Tuist | ⚠️ partial | SPM – глубокий (модульная архитектура на пакетах); Tuist не в истории |
| Swift Testing, XCTest и SnapshotTesting | ⚠️ partial | XCTest + Swift Testing (серия митапов о миграции XCTest → Swift Testing), ViewInspector; SnapshotTesting нет |
| Настройка GitLab CI/CD и Fastlane | ⚠️ partial | CI/CD – Azure DevOps, Bitrise, GitHub Actions («участвовал в развитии CI/CD процессов»); GitLab/Fastlane нет |
| Автоматизация на Swift, Bash, Python | ⚠️ partial | Автоматизация через AI-assisted SDLC (валидационные циклы, тесты, ревью); прямой Bash/Python-автоматизации в CV нет |
| Участие в развитии дизайн-системы | ⚠️ partial | Кастомные UI-компоненты главного экрана (Mega Chips), интерактивные widgets 1M+, инициативные UI/UX-предложения |
| Проведение code review | ✅ full | Регулярные code review (и внутренних, и студентов курсов), технический интервьюер |

**score_nice = (3 × 1.0 + 5 × 0.5) / 8 = 5.5 / 8 = 0.6875**

## Гэпы и что с ними делать

- **GitLab CI/Fastlane + Tuist** → не выдумывать; опираться на реальные CI-практики (Bitrise/Azure DevOps/GitHub Actions, развитие сборки и стабильности) и сформулировать как раннюю готовность к GitLab+Fastlane+Tuist при большом переносимом опыте CI и модульных графов SPM.
- **SnapshotTesting** → смежное: ViewInspector (UI-проверки), автотест-покрытие 75%, серия внутренних митапов о переходе на Swift Testing; реальные snapshot-тесты – быстрый подтягиваемый навык.
- **RxSwift в ежедневном стеке** → практическая миграция RxSwift → Combine сделана «от и до» (Stream Vision 2), но текущий ежедневный стек – Combine/Swift Concurrency; на интервью вести честно: миграцию Rx-слоя делал руками, свежих Rx-проектов в ежедневной практике нет.

## Что подсветить

- RxSwift-миграция как прямое совпадение: целую миграцию RxSwift → Combine завершил с 100% функциональности (+ постепенная UIKit → SwiftUI) – ответ на их центральный «разбираем legacy».
- Масштаб и надёжность продукта: 160K+/500K+ DAU, 99.8% crash-free, 1M+ взаимодействий с виджетами – ответ на «крупное модульное приложение для миллионов клиентов».
- Тестируемость: 13% → 75%, Swift Testing/XCTest/ViewInspector – ответ на «unit- и snapshot-тесты» и покрытие 70–95% у них.
- Архитектура: модульность на SPM, MVVM/Clean, проектирование API и модулей.
- Code review и развитие практик: постоянный ревью, менторство, тех-интервью, собственные митапы.
