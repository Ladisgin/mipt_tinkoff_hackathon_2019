## mipt_tinkoff_hackathon_2019

Проект по обработке пользовательских поисковых запросов в категориях "еда" и "спорт".

В результате работы были выделены 9 намерений пользователе (6 в категории "спорт" и 3 в категории "интенты").

В папке `dictionaries` содержатся составленные и обработанные словари для каждого интента.
В папке ??? данные парсинга сайтов.
Создание датасета: Create_dataset 
Поиск слов запроса по словарям: preclassifier
Поиск с помощью lstm: intent_classification_lstm
Слотфиллинг и составление запроса: Slotfilling
