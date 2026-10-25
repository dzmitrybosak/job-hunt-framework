# Prompt: achievement bullets с цифрами

Исходный промпт — сохранён как есть:

> вот моя текущая роль и компания:
> роль: [роль]
> компания: [компания + индустрия]
> длительность: [время]
> вот мои текущие bullets:
> [paste 3–5 bullets как есть]
> переформулируй каждый bullet в формате:
> [action verb] + [scope/scale] + [result with number] + [tool/method]
> пример хорошего bullet:
> «led migration to GA4 across 40 B2B clients, reducing reporting time 60% using Mixpanel + custom dashboards»
> если в моих bullets нет конкретных цифр — задай мне 3 вопроса, которые помогут вытащить цифры из памяти
> тон: factual, без adjective-ов типа successfully / efficiently / effectively

## Как выполняем в job-hunt

Подстановки: см. `_common.md`. Если просишь про конкретную роль — берём её; если нет — спрашиваем, какую из Experience разбираем.

**Вход:** Experience-блок роли из `profile/master-cv-{ru|en}.md`, `profile/achievements.md`
**Выход:** переписанные bullets → в чат; после твоего подтверждения — в `profile/achievements.md` (и в Experience master-cv, если просишь). Мастер-CV без подтверждения не трогаем.
**Применение:** наполнение банка achievements (общий случай) и блок Key achievements в `resume-adapted.md`. В флоу 1 bullets **не переписываются заново**: берутся из готового банка (и Experience) как есть; правка формулировки – только если нужна адаптация под вакансию (лексика JD, язык резюме). Блок Key achievements собирается полным списком по проектам – готовым к copy-paste в резюме.

## Шаги

1. Взять 3–5 текущих bullets роли «как есть».
2. Проверить каждый на наличие конкретной цифры.
3. **Есть цифры** → переписать в формате `[action verb] + [scope/scale] + [result with number] + [tool/method]`.
4. **Нет цифр** → сначала задать ровно 3 вопроса, чтобы вытащить цифры из памяти. Направления вопросов (выбрать 3 самых подходящих):
   - масштаб: сколько клиентов/пользователей/сервисов/экранов/релизов затронуто?
   - до/после: что ускорилось/сократилось/выросло и на сколько (%, разы, часы, деньги)?
   - частота/объём: сколько в единицу времени (дней, деплоев, запросов, тикетов)?
5. Получил ответы → вернуться к шагу 3. Пользователь не знает цифру → честно «N/A», bullet переписывается без выдуманного числа (scope/scale вместо result).

## Правила

- Формат каждого bullet: `action verb` (past tense: led, built, cut, shipped...) + `scope/scale` + `result with number` + `tool/method`. Один bullet — одно достижение.
- Тон: factual. Запрещённые слова-заглушки: successfully, efficiently, effectively (и семейство: seamlessly, robustly, significantly без цифры).
- Пример из исходного промпта — эталон качества, использовать его стиль.
