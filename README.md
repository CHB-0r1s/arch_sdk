# Python sdk для Arch Linux

1) Утилита для автоматической настройки Bluetooth на Arch Linux.

## Установка с GitHub

### Установка напрямую с GitHub:

```bash
pip install git+https://github.com/CHB-0r1s/bluetooth_setup.git
```

### Установка конкретной версии (релиз):

```bash
pip install git+https://github.com/ВАШ_USERNAME/bluetooth_setup.git@v0.1.0
```

### Установка в режиме разработки:

```bash
git clone https://github.com/ВАШ_USERNAME/bluetooth_setup.git
cd bluetooth_setup
pip install -e .
```

## Использование

После установки команда `bluetooth_setup` будет доступна в консоли:

```bash
bluetooth_setup
```

## Проверка зависимостей

Проект автоматически проверяет соответствие зависимостей из `pyproject.toml` пакетам, доступным в pacman репозиториях Arch Linux.

### Локальная проверка

Для проверки зависимостей локально:

```bash
# Установите tomli, если используете Python < 3.11
pip install tomli

# Запустите проверку
python3 check_pacman_deps.py
```

### CI/CD

При каждом push и pull request автоматически запускается проверка через GitHub Actions. Workflow использует Docker контейнер с Arch Linux для проверки доступности пакетов в pacman репозиториях.
