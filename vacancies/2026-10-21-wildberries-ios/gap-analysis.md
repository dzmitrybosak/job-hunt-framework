# Gap analysis – Wildberries / iOS разработчик в WB Chat

- Режим: A (по JD)
- Дата: 2026-10-21
- Ссылка: – (paste)

## Match: 93% – strong fit

Расчёт: must 1.0 × 0.7 + nice 0.75 × 0.3 = 0.7 + 0.225 = 0.925 → **93%**

JD короткий и по сути совпадает с профилем: Swift высокого уровня, high-load, сложная бизнес-логика, идейность, ответственность, от 5 лет – всё это уже есть в CV с цифрами. Основные зазоры – доменный опыт мессенджера (чаты/синхронизация) и медиа-фичи (голосовые, аудиозвонки), плюс формат «in-house в большой продуктовой компании» (сейчас – долгие продуктовые проекты в консалтинге). Главное действие: подсветить real-time/WebRTC/нотификации и ownership фич, в первом письме уточнить вилку и оформление из BY.

## Must-have

| Требование | Статус | Что из CV использовать |
|---|---|---|
| Владение Swift на высоком уровне | ✅ full | Swift – основной язык 7+ лет; SwiftUI, UIKit, Swift Concurrency, Combine в Core skills и в Experience (Access Management Platform, Stream Vision 2, Between) |
| Опыт на high-load больших проектах | ✅ full | Property & Access Management Platform – 500K+ DAU; Access Management Platform – 160K+ DAU; виджеты с 1M+ взаимодействий при тяжёлой нагрузке |
| Опыт со сложной бизнес-логикой | ✅ full | Guest Passes (несколько backend-сервисов + сложные правила + динамический UI), access flows с permissions/restrictions, client-backend state sync |
| Готовность предлагать идеи по совершенствованию | ✅ full | «Actively contributed to the product design process by proposing UI/UX enhancements», «Took initiative in defining user behaviors when requirements were incomplete», trainer/mentor |
| Высокий уровень ответственности | ✅ full | Ownership фич и analytics/tracking end-to-end, вклад в 99.8% crash-free, менторство, тех. интервьюер, поддержка релиза Stream Vision 2 |
| От 5 лет коммерческого опыта | ✅ full | 7+ лет: Orangesoft 01/2019–10/2021, Coherent Solutions 10/2021–Present (Senior iOS) |

**score_must = 6 × 1.0 / 6 = 1.0**

## Nice-to-have

| Требование | Статус | Комментарий |
|---|---|---|
| Проектирование архитектуры приложения (из «Вам предстоит») | ✅ full | Feature-based modular architecture (SPM, MVVM, Clean Architecture), scalable analytics architecture, client-side sync design; в JD про это прямо |
| Code review | ✅ full | Regular code reviews (Training Center, менторство), PR review как часть AI-SDLC validation loop, тех. интервью |
| Кросс-функциональная работа (QA, дизайнеры, менеджеры, аналитики) | ✅ full | Команды с QA Manual & Automation, BA, UX Designer; работа с дизайном и аналитикой через tracking/event validation |
| SwiftUI / современный стек для нового продукта | ✅ full | SwiftUI в продакшене (Access Management Platform, Between), ongoing UIKit→SwiftUI migration |
| Домен мессенджера (чаты, синхронизация сообщений, offline) | ⚠️ partial | Есть real-time: WebRTC video calling, real-time notifications, distributed backend sync, client-backend state synchronization. Нет прямого опыта с chat/messaging product (сообщения, ленты чатов, delivery/offline queue) |
| Медиа-фичи: аудиозвонки, голосовые, предпросмотр медиа | ⚠️ partial | AVFoundation: photo viewer, video editor (trim/export), media processing; WebRTC video calling; preview media через gallery/stream. Нет аудиозвонков и голосовых сообщений |
| In-house продукт в компании масштаба WB | ⚠️ partial | Долгие продуктовые ownership-проекты в Coherent Solutions (4+ года на одном аккаунте, 500K/160K DAU), но формально это консалтинг, не in-house у маркетплейса |

**score_nice = (1+1+1+1+0.5+0.5+0.5) / 7 = 5.5 / 7 ≈ 0.79**

Match = 0.7 × 1.0 + 0.3 × 0.79 = 0.7 + 0.236 = 0.936 → **93%** (округление вниз, консервативно)

## Гэпы и что с ними делать

- **Домен мессенджера** → закрыть реальным real-time опытом (WebRTC, нотификации, sync); не выдумывать chat-продукт, но показать, что механики те же. Подтянуть быстро: разобрать архитектуру Telegram/WhatsApp публичных докладов перед интервью.
- **Аудиозвонки / голосовые** → закрыть AVFoundation + WebRTC video calling как смежный медиа-стек; честно сказать, что голосовых не делал, но медиа-пайплайн и real-time коммуникации – есть.
- **In-house в большой продуктовой компании** → подчеркнуть долгосрочный ownership продукта (4+ года на платформах с DAU, полный цикл фич) как «продуктовую» историю, а не «аутсорс-разработку»; обсудить на интервью, как устроено product ownership в WB Chat.

## Что подсветить

- Масштаб и надёжность: 160K/500K+ DAU, 99.8% crash-free, 1M+ widget interactions – прямой ответ на «высоконагруженные большие проекты».
- Сложная логика: Guest Passes, permissions/restrictions, multi-backend orchestration – прямой ответ на «сложная бизнес-логика».
- Архитектура и идейность: feature-based modularization (SPM), UI/UX предложения, инициатива при неполных требованиях, code review.
- Real-time: WebRTC video calling, real-time notifications, distributed backend – ближайший опыт к механикам мессенджера.
- Стабильность и ownership: 4+ года на одной продуктовой линии, trainer/менторство/интервью – «высокий уровень ответственности».
