#!/usr/bin/env python3
"""
Скрипт для проверки соответствия зависимостей из pyproject.toml
пакетам, доступным в pacman репозиториях Arch Linux.
"""
import subprocess
import sys
import re
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python < 3.11


def parse_dependencies(pyproject_path):
    """Парсит зависимости из pyproject.toml"""
    with open(pyproject_path, 'rb') as f:
        data = tomllib.load(f)
    
    dependencies = data.get('project', {}).get('dependencies', [])
    return dependencies


def normalize_package_name(pypi_name):
    """
    Преобразует имя пакета из PyPI в формат pacman.
    Например: 
    tqdm -> python-tqdm
    python-dotenv -> python-dotenv
    """
    # Убираем версии (>=, ==, <= и т.д.)
    name = re.split(r'[>=<!=]', pypi_name)[0].strip()
    
    # Если имя уже начинается с python-, используем его как есть
    if name.startswith('python-'):
        pacman_name = name
    else:
        # Преобразуем в формат pacman
        # Обычно Python пакеты в pacman имеют префикс python-
        pacman_name = f"python-{name}"
    
    return name, pacman_name


def check_package_in_pacman(package_name):
    """
    Проверяет, существует ли пакет в pacman репозиториях.
    Возвращает True, если пакет найден, иначе False.
    """
    try:
        # Используем pacman -Ss для поиска пакета
        result = subprocess.run(
            ['pacman', '-Ss', f'^{package_name}$'],
            capture_output=True,
            text=True,
            check=False
        )
        # Если пакет найден, вывод будет непустым
        return bool(result.stdout.strip())
    except FileNotFoundError:
        print("Ошибка: pacman не найден. Убедитесь, что вы на Arch Linux.", file=sys.stderr)
        sys.exit(1)


def main():
    pyproject_path = Path('pyproject.toml')
    
    if not pyproject_path.exists():
        print(f"Ошибка: {pyproject_path} не найден", file=sys.stderr)
        sys.exit(1)
    
    dependencies = parse_dependencies(pyproject_path)
    
    if not dependencies:
        print("Зависимости не найдены в pyproject.toml")
        return 0
    
    print("Проверка соответствия зависимостей пакетам в pacman...\n")
    
    errors = []
    warnings = []
    
    for dep in dependencies:
        _, pacman_name = normalize_package_name(dep)
        found = check_package_in_pacman(pacman_name)
        
        if found:
            print(f"✓ {dep} -> {pacman_name} найден")
        else:
            errors.append(f"❌ {dep} -> {pacman_name} не найден в pacman репозиториях")
    
    print()
    
    if warnings:
        print("Предупреждения:")
        for warning in warnings:
            print(f"  {warning}")
        print()
    
    if errors:
        print("Ошибки:")
        for error in errors:
            print(f"  {error}")
        print(f"\nВсего ошибок: {len(errors)}")
        return 1
    
    print("✓ Все зависимости соответствуют пакетам в pacman!")
    return 0


if __name__ == '__main__':
    sys.exit(main())

