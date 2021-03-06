# mipt_tinkoff_hackathon_2019

Проект выполнен командой `А это обязательный вопрос?` в рамках хакатона `Absolute intelligence` на зимней школе МФТИ по искусственному интеллекту. Проект предоставлен компанией `Tinkoff`.

Задача заключалась в обработке пользовательских поисковых запросов в категориях `еда` и `спорт`.

## Описание работы и структуры файлов
В результате работы были выделены 9 намерений пользователей.

В категории `спорт`:
* buy_sportswear - купить спорт. одежду и обувь
* buy_sport_food - купить спортпит
* buy_equipment - купить снаряжение и инвентарь
* get_service - посетить фитнес-центр, бассейн, зал и т.п.
* get_train - получить услуги инструктора
* rent_equipment - арендовать снаряжение и экипировку

В категории `еда`:
* buy_or_order_goods - купить or заказать доставку продуктов
* buy_food - купить еду в ресторане, баре, кафе и т.д.
* order_food - заказать доставку еды из ресторана, бара, кафе и т.д.

В папке `dictionaries` содержатся составленные и обработанные словари для каждого интента.

В файле `preclassifier.ipynb` содержится код обработки словарей (лемматизация и стемминг) и код предварительного классификатора.

Файлы `dataset.csv` и `Create_dataset.ipynb` относятся к подготовке данных для классификатора LSTM. Код самого классификатора описан в файле `intent_classification_lstm.ipynb`.

В файле `model.h5` содержится сохраненная модель классификатора LSTM.

Файл `slotfilling.ipynb` содержит код выделения ключевых слов из запроса, заполнения слотов для дальнейшего поиска релевантных предложений и составления итогового запроса.

В папке `data` содержатся скрипты, используемые для парсинга сайтов и полученные в результате данные парсинга.

