# rudn_survey_bot
Инструкция по добавлению нового исследования:
1. В файле database.db.py sql_start добавить новую таблицу
2. В файле database.db.py создать асинхронную функцию add_research_for_*название исследования*(state)
3. В файле database.db.py создать функцию download_database_*название исследования*()
4. В пакете handlers создать файл *название исследования*.py
5. В файл keyboards.user_keyboards добавить кнопку для исследования *название исследования*
6. В файле handlers.*название исследования*.py прописать машину состояний по аналогии с test_research_1
7. В пакете keyboards создать файл *название исследования*_keyboard.py
8. В файле keyboards.*название исследования*_keyboard.py создать необходимые для исследования клавиатуры по аналогии с test_research_1_keyboard.py
9. Клавиатуры из keyboards.*название исследования*_keyboard.py должны быть импортированы в handlers.*название исследования*.py
10. В файле main.py зарегистрировать хендлеры опроса
11. В файл keyboards.admin_keyboards.py в клавиатуру choose_db_for_download_keyboard добавить кнопку для загрузки базы данных
12. В файл handlers.admin_handlers.py добавить функцию download_*название исследования*_table(callback: types.CallbackQuery), зерегистрировать хендлер внизу файла
