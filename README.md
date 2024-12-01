# Task for Ritm

## Описание проекта
В проекте изложены решения тестовых заданий с покрытием функций автоматизированными тестами.  
Перед запуском проекта необходима установка всех модулей из файла requirements.txt командой:
   > pip install -r requirements.txt

## Структура проекта
```
Task_for_Ritm/  
    |-- articles.json           # Файл для хранения данных парсинга по заданию 3  
    |-- task_1.py               # Файл с решением задания 1  
    |-- task_2.py               # Файл с решением задания 2  
    |-- task_3.py               # Файл с решением задания 3  
    |-- README.md               # Документация проекта  
    |-- requirements.txt        # Файл с необходимыми модулями для корректной работы приложения  
    Tests/  
        |-- test_task_1.py     # Файл с тестами задания 1 для pytest  
        |-- test_task_2.py     # Файл с тестами задания 2 для pytest  
        |-- test_task_3.py     # Файл с тестами задания 3 для pytest + selenium  
```

## Тестирование
Проект использует pytest для автоматического тестирования:
- Команда для запуска тестов
    > pytest
- Команда, чтобы узнать процент покрытия кода тестами и отображения данных в консоли
    > python -m pytest --cov
  