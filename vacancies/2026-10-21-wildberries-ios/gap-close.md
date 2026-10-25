# Gap close – Wildberries / iOS разработчик в WB Chat

Дата: 2026-10-21
На основе: gap-analysis от 2026-10-21 (Match 93% – strong fit)

## Пробел 1: домен мессенджера (чаты, синхронизация сообщений, offline) – nice-to-have ⚠️

Прямого chat/messaging-продукта в истории нет, и выдумывать его не нужно. Ближайший реальный опыт – real-time слой и синхронизация клиент-сервер в распределённом backend: WebRTC video calling, real-time notifications, client-backend state synchronization и multi-service orchestration в access management. Механики мессенджера (сообщения, delivery, unread state, offline queue) строятся на тех же паттернах синхронизации и event-driven коммуникации; это стоит сказать прямо, не притворяясь, что «писал Telegram».

- Designed client-side synchronization between mobile apps, user accounts, and distributed backend APIs, covering multi-service state updates and error handling for a product serving 500K+ daily active users (Combine, REST, Firebase).
- Developed and evolved real-time user flows – push notifications and WebRTC video calling – within a distributed backend architecture for a 160K+ DAU platform (Swift Concurrency, Combine, Firebase, WebRTC).
- Engineered a scalable analytics architecture with full event tracking for every new feature from day one, validating events end-to-end – the same state/versioning thinking that powers chat sync and delivery guarantees.

## Пробел 2: медиа-фичи – аудиозвонки, голосовые сообщения, предпросмотр медиа – nice-to-have ⚠️

Аудиозвонков и голосовых сообщений в продакшене не делал – это честный partial. Закрываем смежным медиа-стеком: полный цикл медиа-опыта на AVFoundation (просмотр фото, редактор видео с trim/export, обработка файлов), WebRTC video calling как реальный real-time media pipeline, и адаптацию медиа-контента под разные формфакторы (iPad Split View, галереи, preview). Для голосовых можно сказать, что AVFoundation/AudioUnit-стек и опыт с real-time передачей медиа переносятся, а доменные механики (waveform, recording UX) – быстро закрываются, это не архитектурный гэп.

- Designed and implemented media experiences, including a photo viewer and video editing with trimming and export, using AVFoundation and media processing workflows (Stream Vision 2, App Store release).
- Contributed to real-time video calling experiences over WebRTC within a distributed platform, including media handling and connection reliability for 160K+ DAU (WebRTC, Combine, Swift Concurrency).
- Developed key product UI for media-heavy flows – live viewfinder, gallery, preview and device management – integrating media APIs into dynamic application states (UIKit, AVFoundation, CoreStore).

## Пробел 3: in-house продукт в компании масштаба WB – nice-to-have ⚠️

Формально последние 5 лет – консалтинг (Coherent Solutions / ISsoft), а не in-house у маркетплейса. Это лёгкий организационный гэп, не технический: продуктом ownership был полным – 4+ года на одной линии NDA-платформ (от 500K DAU к 160K DAU), ответственность за фичи, метрики, стабильность и качество от архитектуры до production logs. На интервью честно сказать про консалтинг, но показать продуктовый масштаб: долгий horizon, DAU-метрики, влияние на roadmap через UI/UX-предложения и инициативу при неполных требованиях.

- Owned business-critical features end-to-end on multi-year product platforms serving 500K+ and 160K+ daily active users – from architecture and event validation to production log analysis and post-release reliability (99.8% crash-free).
- Took initiative in defining user behaviors when requirements were incomplete and proposed UI/UX improvements in the product design process, influencing roadmap beyond pure implementation.
- Acted as technical interviewer and internal trainer (Swift & iOS course), reviewing code and mentoring engineers – ownership of team quality, not only tickets.

## Что не закрывается (честно)

- **Продакшн-опыт с голосовыми сообщениями и аудиозвонками** → компенсация: показать медиа-стек (AVFoundation: video editor/viewer) и real-time WebRTC video calling как смежную базу; на интервью честно сказать, что голосовых не делал, и предложить quick plan (AVAudioEngine/recording, waveform UI, media upload pipeline) как домашнее задание или первый спринт.
- **Опыт с chat-спецификой delivery/offline queues на масштабе мессенджера** → компенсация: до отклика/до интервью разобрать 1–2 публичных разбора архитектуры мессенджеров (Telegram/WhatsApp engineering blogs) и подготовить вопросы к команде WB Chat про sync, unread, media cache, push; не выдумывать опыт, а признать gap и показать подготовленность.
- **In-house статус у компании размера WB** → компенсация: не спорить с фактом, но перевести разговор на продуктовый ownership и масштаб (DAU, стабильность, roadmap-влияние); уточнить, как устроено распределение ответственности в команде WB Chat.
