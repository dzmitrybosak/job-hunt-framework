# Gap analysis – SKIES (Kasari Lab, UCLA) / iOS Developer Embedded

Дата: 2026-10-21
Режим: A (по JD)
Ссылка: paste (julius@skieslearn.com)

## Match: 70% – good fit

Расчёт: must 0.75 × 0.7 + nice 0.58 × 0.3 = 0.525 + 0.175 = **0.70**

Сильное техническое совпадение (shipped native iOS, AI-force-multiplier, large/maintainable systems) тянет скор вверх; domain (autism / AAC / clinical research) и «embedded in a lab» – частичные или пустые. **Отдельный жёсткий гейт вне Match %: «In person at UCLA» (Los Angeles) – не совпадает с профилем (remote из Беларуси / onsite в Беларуси, релокация не рассматривается). Без удалёнки отклик не имеет смысла, какой бы ни был Match %.**

## Вердикт

Технически это good fit: три из шести must-have закрыты полностью, три – partial (soft skills / lab-adjacent). Ключевые nice-to-have из домена (AAC, autism intervention, NIH SBIR) – гэпы. Реалистичный сценарий: сильный отклик с честной мотивацией, если SKIES готовы к удалёнке/гибриду; иначе – фиксируем как «passed on location».

## Must-have

| # | Требование (JD «ideal candidate») | Статус | Что из CV использовать |
|---|---|---|---|
| 1 | Comfortable being close to researchers/clinicians, takes feedback | ⚠️ partial | Работа с BA / UX Designer / product design process (A4 «Actively contributed to the product design process by proposing UI/UX enhancements and resolving interface ambiguities»), тренерство и тех. интервью в Coherent; research-среды нет |
| 2 | Shipped real native iOS apps | ✅ full | Stream Vision 2 (App Store id1511736862), Between: Decision Journal (App Store), Property & Access 500K+ DAU, Access Management 160K+ DAU |
| 3 | Uses AI as force multiplier, understands code, not dependent | ✅ full | AI-SDLC в Summary и A-bullets: spec-driven, project-specific AI rules, validation loop (compile / tests / SwiftLint / static analysis / review / CI), Cursor, Codex, Copilot |
| 4 | Builds large and complex yet maintainable systems | ✅ full | Feature-based modularization (SPM) + MVVM + Clean Architecture (A: «reducing coupling… improving application scalability and maintainability»), A2 тесты 13% → 75% |
| 5 | Resourceful, motivated, tenacious | ⚠️ partial | Solo end-to-end ship Between (весь продукт + Swift backend + StoreKit), 0-to-1 версия Stream Vision 2, «Beyond Projects Scope» (trainer / mentor / interviewer); soft skill |
| 6 | Calm, respectful presence in a research lab | ⚠️ partial | Trainer + mentor + тех. интервьюер (soft evidence уважительного общения); прямого опыта research lab нет |

score_must = (0.5 + 1 + 1 + 1 + 0.5 + 0.5) / 6 = 4.5 / 6 = **0.75**

## Nice-to-have

| # | Требование | Статус | Комментарий |
|---|---|---|---|
| 1 | Native iOS / Swift depth (SwiftUI, UIKit) | ✅ full | 7+ лет Swift, SwiftUI + UIKit, Swift Concurrency, Apple-экосистема |
| 2 | Assistive tech / AAC / autism / early intervention domain | ❌ gap | Опыта в домене нет (в прошлом: IoT / access management / retail / sports / real estate / productivity) |
| 3 | Clinical / research / NIH-SBIR collaboration | ❌ gap | Нет опыта в research lab / с clinician stakeholders / с грантовыми фазами |
| 4 | Child- and clinician-facing UX craft («delightful», usable mid-play) | ⚠️ partial | Сильный UI-craft (Mega Chips, Guest Passes, live viewfinder, interactive widgets, media experiences, UIKit→SwiftUI migration) + UX-сотрудничество; но не в clinical-контексте «use while playing with a child» |
| 5 | 0-to-1 prototype in small team (Phase I speed) | ✅ full | Stream Vision 2 «built the app version from scratch that shipped to the App Store», solo Between (App Store), команды 2 iOS |
| 6 | English working proficiency | ✅ full | B2 (Upper-Intermediate) |

score_nice = (1 + 0 + 0 + 0.5 + 1 + 1) / 6 = 3.5 / 6 = **0.58**

## Гэпы и что с ними делать

- **Гэп 1 (nice ❌, высокая боль): AAC / autism / early intervention domain** → компенсировать: зафиксировать продуктовую близость (коммуникация, assistive-намеки, accessibility, «простое решение сложной задачи» – AVFoundation/media, UX с ambiguities), честно сказать «domain новый, но я готов глубоко погрузиться» + подчеркнуть скорость погружения (AI-SDLC). Не притворяться специалистом по JASPER.
- **Гэп 2 (must ⚠️, высокая боль): работа в связке с researchers/clinicians** → переформулировать существующий feedback-loop опыт (BA / UX / product design, resolving interface ambiguities, mentorship) + явно сказать в cover letter, что формат «close to clinicians» – то, что я хочу, а не что терплю.
- **Гэп 3 (nice ❌): NIH SBIR / academic research setting** → не закрывается опытом. Компенсация: сильная мотивация к миссии + вопрос на интервью про milestone plan Phase I; показать, что умею работать с ограничениями (6 мес. deadline, research constraints) через shipped deadlines (0-to-1 релизы).
- **Гэп 4 (гейт, не skill): локация** → не закрывается опытом. Компенсация: поднять вопрос «удалённо / hybrid / периодические визиты» первым же письмом; если строго onsite – зафиксировать отказ.
- **Гэп 5 (nice ⚠️): UX «use while playing with a child»** → не подсвечивать как domain-опыт; показать навык «динамическое UI под неопределённые требования» (Guest Passes, Mega Chips, live viewfinder) и готовность тестировать с клиницистами.

## Что подсветить

- **Shipped native iOS in App Store:** Stream Vision 2 (1.2K ratings, 4.7/5) + Between: Decision Journal (solo end-to-end) + два крупных продукта в Coherent (500K+ / 160K+ DAU) – прямой ответ на «has shipped real native iOS apps».
- **AI as force multiplier:** AI-SDLC в master-cv (Summary + A-bullets) – прямой ответ на третий пункт JD, редкое совпадение по формулировке.
- **Large / complex / maintainable:** modular SPM + Clean Architecture + тесты 13% → 75% – прямой ответ на четвёртый пункт JD.
- **0-to-1 + small team:** Stream Vision 2 с нуля до App Store, solo Between – релевантно Phase I («если прототип сработает»).
- **Accessibility-намёки:** Watch companion, CarPlay, Widgets, «iPad Split View and different screen configurations», «proposing UI/UX enhancements» – soft-связь с assistive-продуктом, не domain-claim.
- **Мотивация к миссии:** в cover letter коротко и честно, без фальши, – JD прямо спрашивает «does that evoke something in you».
