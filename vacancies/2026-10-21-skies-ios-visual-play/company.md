# Company research – SKIES (Su-Kam Intelligent Education Systems) / Kasari Lab, UCLA

Дата: 2026-10-21
Источники:
- [Visual Choices AAC – App Store](https://apps.apple.com/us/app/visual-choices-aac/id6448635588) (primary, verified 2026-10-21)
- [Skies Learn – App Store](https://apps.apple.com/us/app/skies-learn/id919049298) (primary, verified 2026-10-21)
- [Kasari Lab at UCLA](https://www.kasarilab.org/) / [JASPER](https://www.jaspertraining.org/) / [Connie Kasari – UCLA SEIS](https://seis.ucla.edu/faculty/connie-kasari/) (secondary, snippets)
- JD (paste, 2026-10-21) – источник по Visual Play / SBIR / условиям
- LinkedIn job (secondary, snippet): https://www.linkedin.com/jobs/view/ios-developer-embedded-at-a-ucla-autism-lab-at-skies-inc-4468405570 (там же «SKIES Inc» как legal name)

## TL;DR

SKIES (юридическое имя в App Store: Su-Kam Intelligent Education Systems Inc, Pasadena, основана аlumni Caltech) – маленькая компания, которая делает коммуникационные/обучающие приложения для людей с особыми потребностями. Флагман: Visual Choices AAC – активно развиваемый AAC для «early communicators» с аутизмом (4.79/5, 163 оценки, последний апдейт 2026-10-15). Сейчас набирают iOS-разработчика в NIH SBIR Phase I на новый продукт Visual Play совместно с Kasari Lab UCLA (JASPER-интервенция). Стоит времени как mission-driven / research-adjacent контракт, но формат «in person at UCLA» – блокер для профиля без релокации.

## Продукт и рынок

- **Visual Choices AAC** (iOS, free, Education + Medical): «an easy way to communicate, and develops natural speech», для early communicators с аутизмом. Делали с early intervention experts; используют speech therapists, special education teachers, clinical directors, parents. Ключевые фичи: выборы на фото, lip animations + visual phonics, интегрированный AAC + signing videos, доступ к 50 000+ SymbolStix, type/dictate в sentence bar, voice-to-highlight, voice-to-choices, печать boards (no-tech), eye gaze (hands-free), работает offline, поддержка английского и испанского (фрагмент из описания).
- **Рынок:** AAC / assistive communication для аутизма и early intervention – нишевый, clinical + family; конкуренты по категории (Visuals2Go, PictoCue и др.) – факт из App Store search.
- **Visual Play** (в разработке, ещё нет в App Store): NIH SBIR Phase I (6 месяцев) – «a delightful app that takes pieces of this intervention, and others, and makes them easier for regular clinicians to do». Поставка через клинику: clinician использует приложение, играя с ребёнком.
- **Skies Learn** (2017): collaborative lessons / class bulletin board (Education + Productivity, 3.0/5, 91 оценка) – более старый продукт той же компании, сегодня на второй роли.

## Технологии и стек

- **iOS-стек SKIES:** нет публичных данных (нет открытого engineering blog / open source по SKIES). Факты только из JD: «real native iOS apps» (т.е. native, не cross-platform).
- **Продуктовые технологические маркеры Visual Choices:** SymbolStix API, AAC sentence bar, lip/phonics animation, eye gaze, offline-first, печать boards, voice input – намекает на плотный UIKit/SwiftUI + AVFoundation/speech + accessibility-stack.
- **Visual Play (новое):** стек не раскрыт; JD подчёркивает «AI as a force multiplier» и «large and complex, yet maintainable, systems».

## Команда и культура

- SKIES – «small Pasadena company started by Caltech alums» (JD). Размер инженерной команды: нет данных.
- **Контакт в JD:** julius@skieslearn.com (роль человека не указана – предположительно hiring / ops для SBIR).
- **Kasari Lab (UCLA)** – «one of the top autism research groups in the world» (JD); по вторичным источникам: Connie Kasari, UCLA faculty с 1990, founding member of Center for Autism Research and Treatment at UCLA; создатель JASPER (Joint Attention Symbolic Play Engagement and Regulation) – play-based intervention для social communication у детей с аутизмом; lab работает в тесном контакте с local community, parents, teachers (kasarilab.org snippet).
- **Модель работы по JD:** «Embedded in the lab from Day 1, paired with an implementation lead who spends their weeks with clinicians» – не продуктовая команда в вакууме, а co-location с исследователями/клиницистами.
- Glassdoor / DOU отзывы: нет данных.

## Процесс найма

- Прямой контакт: email julius@skieslearn.com («Interested? Contact...») – без ATS, без портфолио-формы. «Starting as soon as we find the right person» – быстрый старт, найм не по формальному циклу.
- Этапы: нет данных (не описаны).

## Флаги

🟢 **Mission-fit:** реальный вклад в коммуникацию minimally verbal autistic children; NIH SBIR, Kasari Lab – сильный смысловой контекст для cover letter / motivation.
🟢 **Senior-fit по JD:** «shipped real native iOS apps», «AI as a force multiplier» – ровно про master-cv (7+ лет native iOS, AI-SDLC, 500K+ DAU, shipped apps в App Store, включая solo pet-проект Between с AI-features).
🟢 **Small team + влияние:** embedded в lab, pairing с implementation lead – продуктовое влияние без корпоративной иерархии.
🟢 **Финансовая устойчивость контракта:** NIH SBIR Phase I – деньги на 6 мес. уже есть (award), не «стартап без runway».
🟢 **Visual Choices живой продукт:** последний релиз 2026-10-15 – команда реально шипит, а не «прототип 2023 года».
🔴 **Локация (блокер):** «In person at UCLA» – Los Angeles. Профиль: только remote из Беларуси / hybrid-onsite в Беларуси, релокация не рассматривается. Без удалёнки/командировки-исключения отклик не имеет смысла.
🟡 **Срок / тип:** 6 мес. Phase I (SBIR). Phase II «если прототип сработает» – следующий этап не гарантирован.
🟡 **Вилка vs рынок US:** $65,000 за 6 мес. ($130K annualized) – для onsite LA это ниже market senior iOS (SF/LA), но выше профильного порога; учитывать стоимость жизни в LA и relocation.
🟡 **Компания маленькая / нишевая:** нет данных о размере инженерной команды, нет публичного engineering culture – риск «один iOS-разработчик на всё».
🔴 **Миссия-вопрос из JD:** «Does that evoke something in you beyond the number? A personal connection...» – ждут эмоциональной вовлечённости; случайный отклик без мотивации будет заметен.

## Вопросы к ним на интервью

- Какой формат работы на самом деле: строго onsite UCLA 5 дней/внедрён, или допускается hybrid / периодический remote из-за рубежа на время Phase I?
- Что входит в Phase I deliverable: прототип для клиницистов, исследовательский инструмент или pre-App Store product? Критерии «прототип сработал» для Phase II?
- Кто будет использовать Visual Play в лаборатории: клиницисты Kasari Lab, external clinics? Какой feedback loop с implementation lead?
- Какой текущий iOS-стек SKIES (UIKit / SwiftUI / target iOS version / CI / accessibility requirements)? Есть ли codebase Visual Choices, который переиспользуем, или Visual Play с нуля?
- Как организована работа с чувствительными данными детей (HIPAA / FERPA / IRB / data retention)? Есть ли требования к privacy, offline, аудиту?
- Какой размер команды iOS у SKIES сейчас? Кто ещё работает над Visual Play (design, backend, research)?
- Срок Phase I жёсткий (6 мес.) – как выглядит milestone plan (design → prototype → clinician testing)?
- Что происходит с контрактом после Phase I, если Phase II не одобрен?
