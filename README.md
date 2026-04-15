# API тестирование Google Maps

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-8.2.0-blue.svg)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-2.29.0-blue.svg)](https://docs.qameta.io/allure/)

## О проекте

Этот проект — демонстрация моих навыков автоматизации тестирования API. В нем реализован набор автотестов для публичного API Google Maps. Проект служит примером моей работы для портфолио QA Automation.

### 🛠️ Стек технологий

*   **Язык:** Python 3.11
*   **Фреймворк для тестов:** Pytest — для написания и запуска тестов[reference:3].
*   **Библиотека для HTTP-запросов:** Requests — для взаимодействия с API.
*   **Формирование отчётов:** Allure Report — для создания наглядных и информативных отчетов о тестировании.
*   **Логирование:** Кастомный логгер для детального отслеживания шагов выполнения тестов.

### 📋 Содержание проекта

*   `tests/` — директория с тестовыми сценариями.
*   `utils/` — вспомогательные модули:
    *   `api.py` — класс с методами для взаимодействия с API Google Maps.
    *   `checking.py` — класс с методами для проверки ответов (статус-коды, JSON).
    *   `http_methods.py` — обертка над requests для выполнения GET, POST, PUT, DELETE запросов.
    *   `logger.py` — модуль для логирования.
*   `requirements.txt` — файл со всеми зависимостями проекта.
*   `README.md` — файл с описанием проекта (текущий).

### 🚀 Быстрый старт (запуск тестов у себя)

Следуйте этим шагам, чтобы запустить тесты на своем компьютере:

---

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/bogdanxQA/google_maps_api_tests.git
cd google_maps_api_tests
```

---

### 2. Создайте и активируйте виртуальное окружение

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Запустите тесты

```bash
pytest -s -v
```

---

### 5. Сгенерируйте и откройте Allure-отчёт

Если Allure ещё не установлен, воспользуйтесь инструкцией с официального сайта.

Убедитесь, что вы находитесь в корневой папке проекта, затем выполните команду:

```bash
allure serve test_results/
```
