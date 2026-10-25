# Master CV – индекс и общие факты

Master CV хранится в **двух языковых версиях**. Формулировки, цифры и факты брать только из версии, соответствующей языку вакансии (правило выбора – `prompts/output-language.md`):

| Язык вакансии / JD | Файл версии |
|---|---|
| **ru** | `profile/master-cv-ru.md` |
| **en** | `profile/master-cv-en.md` |

Нет JD (флоу 2 / network) → язык сайта компании; неясно → спросить пользователя (не угадывать и не переводить втихую).

В промптах под «master-cv» понимается **выбранная по языку версия** `profile/master-cv-{ru|en}.md`. Формулировки из одной версии не переносить в другую и не переводить при адаптации – только акценты и лексика JD (`prompts/tailor-resume.md`). При копировании в генерируемые тексты действует типографика `_common.md` («–», не «–»).

Источник обновления: файлы «Bosak Dmitry iOS CV ru.md» и «Bosak Dmitry iOS CV.md» (присланы 2026-10-22).

---

## Общие факты (неязыковые, для обеих версий)

### Условия и локация

- Location / timezone: Belarus (UTC+3)
- Open to: remote work from Belarus; hybrid / onsite in Belarus. No relocation.
- GitHub: https://github.com/dzmitrybosak

### Дополнительные факты опыта

Были в master-cv до 2026-10-22; в новых CV-файлах отсутствуют. Использовать как материал для адаптации (gap-close, bullets), ничего нового не достраивая.

Access Management Platform (NDA), Coherent Solutions:

- Engineered a scalable analytics architecture, ensuring every new feature was integrated with comprehensive event tracking from the outset.
- Designed and implemented robust tracking systems, taking ownership of the full cycle from architectural design to event validation, improving data-driven decision-making.
- Actively contributed to the product design process by proposing UI/UX enhancements and resolving interface ambiguities.
- Took initiative in defining user behaviors when requirements were incomplete, ensuring a seamless and intuitive user experience through proactive design solutions.

### Open source / pet projects

#### Between: Decision Journal (pet project, App Store)

- Ссылка: https://apps.apple.com/by/app/between-decision-journal/id6789844562 (Provider: Dzmitry Bosak; Terms: https://dzmitrybosak.github.io/between/terms/)
- Что это: private space to think things through with AI («reflection companion»). Структурированная рефлексия: сложное решение / разговор / чувство → диалог с AI → саммари и key takeaways, разбор ситуации с разных сторон, приватный журнал с напоминаниями, Magic Mode для глубокого разбора, приложение на Apple Watch. Не принимает решение за пользователя: «Not advice. Clarity».
- Моя роль: solo developer – весь продукт от и до (provider в App Store – Dzmitry Bosak).
- Стек: SwiftUI, Swift Concurrency, Observation, Clean Architecture + MVVM (presentation layer), watchOS companion, Swift backend (написан мной), In-App Purchases (StoreKit: Monthly USD 4.99 / Yearly USD 29.99), AI-assisted features.
- Назначение: площадка для опробования новых технологий, в том числе AI.
- Факты из App Store (verified 2026-10-20): version 1.0.2 (Aug 14), rating 5.0/5 (1 rating), category Productivity, iOS 26+, languages English + Russian.
- Планы (только планы, не реализовано): Kotlin Multiplatform, desktop-версия, CoreML.

## Что НЕ писать в резюме (личные предпочтения)

- Оба проекта в Coherent Solutions под NDA: название платформы не раскрывать, описывать домен и масштаб обезличенно.
