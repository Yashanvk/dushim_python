# Тесты на Python
Установка зависимостей 
``` bash
pip install -r requirements.txt
```
Запуск тестов по маркеру 
``` bash
pytest -m capsules
```
## Структура проекта 
``` 
odp-gp-tests/
├── dags/
│   ├── my_calculation_dag.py      # основной расчётный DAG
│   └── my_calculation_tests.py    # DAG/таск с тестами
│
├── tests/                         # тестовая логика, исполняемая Airflow
│   ├── GPconnection.py            # подключение к Greenplum
│   ├── utils.py                   # вспомогательные функции
│   └── cases/
│       ├── test_case_1.sql        # SQL-тесты
│       ├── test_case_2.sql
│       └── ...
│
├── docker-compose.yml             
└── README.md

```