# Gap analysis — OSON / iOS разработчик (Middle)

- Режим: A (по JD)
- Дата: 2026-10-20
- Ссылка: https://oson.com/int-ru/vacancies

## Match: 90% — strong fit

Расчёт: must 0.9 × 0.7 + nice 0.9 × 0.3 (nice-to-have в JD нет → score_nice = score_must)
Технические требования JD закрываются почти полностью: 7+ лет iOS, Swift, UIKit, Firebase, REST, CI/CD – всё есть прямо в CV. Единственные частичные зоны: прямой Core Data (есть CoreStore, который построен поверх Core Data) и явный Agile/Scrum (командная работа с BA/UX/QA есть, но процесс в CV не зафиксирован). Главное действие: уточнить до интервью формат работы и вилку – по ним пока пустота.

## Вердикт

Технически это strong fit – фактически уровень требований ниже нашего опыта. Основные риски не технические: формат работы (нужен remote из Беларуси или hybrid/onsite в Беларуси), не указанная вилка и уровень Middle при 7+ годах опыта. Решение о подаче принимать после ответа рекрутера на эти три вопроса.

## Must-have

| Требование | Статус | Что из CV использовать |
|---|---|---|
| от 2 лет в мобильной разработке | ✅ full | 7+ лет iOS: Orangesoft (01/2019 – 10/2021) + Coherent Solutions (10/2021 – Present) |
| Swift | ✅ full | весь опыт: оба проекта Coherent, Stream Vision 2, pet project Between (Swift backend) |
| Xcode | ✅ full | ежедневный инструмент во всех проектах, включая работу с build time (оптимизация сборок в SV2) |
| UIKit | ✅ full | Property & Access Platform (500K DAU), Stream Vision 2, selected projects; UIKit → SwiftUI миграция в текущем проекте |
| Git | ✅ full | стандартный поток: feature branches, PR, code review (менторство и code review в Coherent/Orangesoft) |
| Firebase | ✅ full | Firebase во всех трёх продуктовых проектах (Coherent оба, Stream Vision 2) |
| Core Data | ⚠️ partial | прямого Core Data нет; CoreStore в Stream Vision 2 – типобезопасная обёртка поверх Core Data (стек данных), плюс Realm в selected projects. Подсветить: знаком с Core Data-моделью через CoreStore |
| Agile/Scrum | ⚠️ partial | косвенно: работа в кросс-функциональных командах с BA, UX, QA (Coherent/Orangesoft); явно в CV не указано. Подсветить: командные процессы, итеративная поставка |
| CI/CD | ✅ full | Azure DevOps, Bitrise, GitHub Actions; AI-SDLC валидационный луп с CI в текущем проекте |
| Интеграция API (REST, JSON) | ✅ full | client-backend синхронизация, distributed backend APIs (Property & Access), REST APIs в Core skills |

## Nice-to-have

| Требование | Статус | Комментарий |
|---|---|---|
| (в JD не выделены) | – | отдельных nice-to-have в JD нет; использован score_must |

## Гэпы и что с ними делать

- **Core Data** → компенсировать: CoreStore в Stream Vision 2 построен поверх Core Data (описать как опыт работы с Core Data-стеком), Realm в других проектах; не подсвечивать как «прямой Core Data», если спросят – честно: «использовал обёртки, Core Data модель понятна» (см. `gap-close.md`).
- **Agile/Scrum** → подсветить: кросс-функциональные команды (BA, UX, QA, manual + automation QA), итеративная поставка фич; уточнить на скрининге свой процессный опыт (какие спринты, роли).
- **Уровень Middle при опыте 7+ лет** → не «гэп», а риск по условиям: обсудить уровень и вилку до технических этапов.
- **Формат работы и вилка не указаны** → не технический гэп, но стоп-фактор: вопрос рекрутеру первым сообщением.

## Что подсветить

- 500K+ и 160K+ DAU продуктовый опыт с фокусом на надёжность (99.8% crash-free) – прямая параллель с платёжным продуктом, где стабильность критична.
- Участие в принятии продуктовых решений (предложения по UI/UX, инициатива по analytics-архитектуре) – для финтех-продукта это плюс.
- Опыт с платежами в pet project Between (StoreKit IAP: Monthly/Yearly) – небольшой, но живой платёжный опыт.
- AI-SDLC опыт (spec-driven, AI-assisted testing/review) – дифференциатор, которого нет у большинства кандидатов на Middle.
