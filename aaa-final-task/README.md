# Pizza CLI

CLI-приложение для заказа пиццы. Требуется Python 3.11+.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
python cli.py menu
python cli.py order pepperoni
python cli.py order pepperoni --delivery
```

## Проверка

```bash
python -m pytest
flake8 .
mypy .
black --check .
```
