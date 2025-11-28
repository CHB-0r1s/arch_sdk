# Python sdk для Arch Linux

1) Утилита для автоматической настройки Bluetooth на Arch Linux.

## Установка с GitHub

### Установка напрямую с GitHub:

```bash
pip install git+https://github.com/CHB-0r1s/arch_sdk.git
```

### Установка конкретной версии (релиз):

```bash
pip install git+https://github.com/CHB-0r1s/arch_sdk.git@v0.1.1
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