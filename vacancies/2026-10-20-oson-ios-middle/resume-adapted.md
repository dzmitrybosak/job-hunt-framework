# Adapted resume — OSON / iOS разработчик (Middle)

Дата: 2026-10-20
Язык: ru

## Summary

iOS-инженер с 7+ годами разработки мобильных приложений на Swift: UIKit, интеграция REST/JSON API, Firebase, Core Data-стек (CoreStore), Xcode, Git, CI/CD (Azure DevOps, Bitrise, GitHub Actions).
Держал стабильность продуктов на 160K+ DAU (99.8% crash-free rate) и поднял покрытие unit-тестами с 13% до 75%, чтобы фичи выпускались безопаснее.
Ищу роль iOS-разработчика в продуктовой команде – интересен финтех-продукт OSON и задачи, где надёжность мобильного клиента напрямую влияет на пользователей.

## Key achievements

### Coherent Solutions (ISsoft) – Senior iOS Developer (10/2021 – настоящее время)

#### Access Management Platform (NDA) (02/2024 – настоящее время)

- Развивал критичные пользовательские сценарии продукта на 160K+ DAU, вкладываясь в 99,8% crash-free rate (Swift, UIKit/SwiftUI, Combine, Firebase).
- Спроектировал и реализовал интерактивные виджеты управления устройствами, набравшие 1M+ пользовательских взаимодействий при стабильной работе под нагрузкой (SwiftUI, WidgetKit, AppIntents).
- Внёс вклад в feature-based модульную архитектуру (Swift Package Manager, MVVM, Clean Architecture), снизив связанность фич и улучшив масштабируемость продукта.
- Поднял покрытие unit-тестов с 13% до 75% и встроил тесты и статические проверки в CI (XCTest, Swift Testing, SwiftLint; Azure DevOps, Bitrise, GitHub Actions).
- Спроектировал масштабируемую аналитическую архитектуру: каждая новая фича получала полное событийное отслеживание с первого дня; доводил tracking от архитектуры до валидации событий.

#### Property & Access Management Platform (NDA) (10/2021 – 02/2024)

- Разработал критичные продуктовые фичи (проходы для гостей, сценарии доступа с правами и ограничениями) для приложения на 500K+ DAU (UIKit, Combine, AVFoundation, Firebase).
- Спроектировал клиентскую синхронизацию между мобильными приложениями, учётными записями и распределёнными backend REST API, включая версионирование контрактов и обработку ошибок.

### Orangesoft Development – iOS Developer (01/2019 – 10/2021)

#### Stream Vision 2 (11/2019 – 10/2021)

- Построил ключевой UI продукта (живой видоискатель, лента новостей, галерея, управление устройствами) и был среди инженеров, собравших версию с нуля и выпустивших её в App Store (UIKit, CoreStore, Firebase, AVFoundation).

### Pet project

#### Between: Decision Journal

- Сольный продукт от идеи до App Store: приватная рефлексия с AI, watchOS companion, монетизация через StoreKit (SwiftUI, Swift Concurrency, Observation, Clean Architecture + MVVM).

## Skills (порядок под вакансию)

- Swift, UIKit, Xcode, Git
- REST/JSON API, Firebase
- Core Data-стек: CoreStore (обёртка над Core Data), Realm
- CI/CD: Azure DevOps, Bitrise, GitHub Actions
- Тестирование: XCTest, Swift Testing, ViewInspector
- MVVM, Clean Architecture, feature-based модульность (Swift Package Manager)
- Swift Concurrency (async/await), GCD, Combine, SwiftUI
- Прочее: AVFoundation, APNs, StoreKit, SonarQube, SwiftLint, Jira, Postman, Charles Proxy
- Командные процессы: кросс-функциональные команды (BA, UX, QA manual + automation), code review, итеративная поставка

## Что изменилось vs master-cv

- Summary: переписан под лексику JD (Swift, UIKit, REST/JSON, Firebase, Core Data, CI/CD) с двумя цифровыми достижениями; AI-SDLC блок опущен вниз по приоритету – в JD его нет.
- Achievements: полный готовый список по проектам (как в content.json / Experience) – A1–A5 и bullets из Experience (модульная архитектура, аналитика, client sync, Stream Vision, Between). Формулировки из банка/Experience; правка только под язык резюме (ru) без изменения фактов и цифр. Stream Vision 2 оставлен в хронологии (01/2019 – 10/2021), как в Experience.
- Skills: порядок переставлен под JD (Swift/UIKit/Xcode/Git → REST/Firebase → Core Data → CI/CD → тесты); добавлены Realm и командные процессы из master-cv.
- Опущено под эту вакансию: подробный AI-SDLC блок (оставлен в master-cv/cv-updated), CarPlay/WatchConnectivity/WidgetKit как отдельные акценты (кроме A1), trainer/менторство/интервьюерство, Beyond Projects Scope.

## Что опущено честно

- Прямого опыта Core Data в проде нет (есть CoreStore поверх Core Data) – см. `gap-close.md`.
- Финтех-домен: платежный опыт только через StoreKit в собственном приложении.
