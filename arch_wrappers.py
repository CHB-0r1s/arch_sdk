#!/usr/bin/env python3
import subprocess
import sys
import os
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv


def load_password():
    """Загружает пароль из .env файла"""
    # Загружаем .env файл
    env_path = Path('.env')
    if not env_path.exists():
        env_example = Path('.env.example')
        if env_example.exists():
            print(f"Ошибка: файл .env не найден. Создайте его на основе {env_example}", file=sys.stderr)
        else:
            print("Ошибка: файл .env не найден. Создайте файл .env с параметром SUDO_PASSWORD", file=sys.stderr)
        sys.exit(1)
    
    load_dotenv()
    password = os.getenv('SUDO_PASSWORD')
    
    if not password:
        print("Ошибка: параметр SUDO_PASSWORD не найден в .env", file=sys.stderr)
        sys.exit(1)
    
    return password.encode()


class PacmanWrapper:
    def __init__(self):
        self.password = load_password()
    def install(self, package):
        subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', package], check=True, input=self.password)
    
    def install_batch(self, packages):
        for package in tqdm(packages, desc="Установка пакетов"):
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', package], check=True, input=self.password)


class SystemctlWrapper:
    def __init__(self):
        self.password = load_password()
    
    def start(self, service):
        subprocess.run(['sudo', 'systemctl', 'start', service], check=True, input=self.password)
    
    def enable(self, service):
        subprocess.run(['sudo', 'systemctl', 'enable', service], check=True, input=self.password)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    pacman = PacmanWrapper()
    pacman.install(sys.argv[1])