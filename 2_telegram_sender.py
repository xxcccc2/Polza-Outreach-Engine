"""
Отправка текста из .txt в Telegram
pip install requests

Настройка:
1. @BotFather -> /newbot -> скопируй токен
2. Добавь бота в чат, напиши что-нибудь
3. Открой https://api.telegram.org/bot<TOKEN>/getUpdates -> найди chat_id
"""

import requests
import sys
import os

BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")
CHAT_ID = os.getenv("TG_CHAT_ID", "")


def send(text: str) -> bool:
    """Отправляет текст в Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    # Разбиваем если >4096 символов
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    
    for chunk in chunks:
        r = requests.post(url, json={"chat_id": CHAT_ID, "text": chunk})
        if not r.json().get("ok"):
            print(f"Ошибка: {r.json()}")
            return False
    return True


def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("Задай переменные окружения:")
        print("  set TG_BOT_TOKEN=123456:ABC...")
        print("  set TG_CHAT_ID=-100123456789")
        return
    
    if len(sys.argv) < 2:
        print("python 2_telegram_sender.py message.txt")
        return
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    text = open(file_path, 'r', encoding='utf-8').read()
    if not text.strip():
        print("Файл пустой")
        return
    
    if send(text):
        print("Отправлено!")
    else:
        print("Не удалось отправить")


if __name__ == "__main__":
    main()
