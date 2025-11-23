Для запуска нужны:
- python 3.13
- tabulate>=0.9.0
- для тестов pytest>=9.0.1

Локальное окружение собиралось через uv


Скришот примера запуска скрипта находится в папке Example файл screen.jpg

## запуск скрипта
- cd корневая папка проекта
- python main.py --files files/employees1.csv --report performance  
---
## структура проекта
```text
project/
│
├── reports/
│   ├── base.py            # базовый класс отчётов
│   ├── performance.py     # отчёт performance
│   └── registry.py        # регистрация отчётов
│
├── reader/
│   └── csv_reader.py      # чтение CSV
│
├── cli.py                 # обработка аргументов
├── main.py                # точка входа
│
└── tests/                 # pytest-тесты
```

