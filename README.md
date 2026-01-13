# Тестовое задание — Polza Outreach Engine

Сделал за ~3 часа. Всё работает, проверял.

---

## Что внутри

| Файл | Что делает |
|------|------------|
| `1_email_checker.py` | Проверка MX-записей доменов |
| `2_telegram_sender.py` | Отправка текста из .txt в Telegram |
| `3_architecture.md` | Архитектура на 1200 ящиков для аутрича |

---

## 1. Email Checker

Проверяет домены на валидность MX-записей. Без лишнего — 30 строк кода.

```bash
pip install dnspython
python 1_email_checker.py "test@gmail.com,fake@notexist.xyz"
```

Вывод:
```
test@gmail.com — домен валиден
fake@notexist.xyz — домен отсутствует
```

Можно скормить файл с email'ами (по одному на строку):
```bash
python 1_email_checker.py emails.txt
```

---

## 2. Telegram Sender

Отправляет текст из файла в Telegram чат. Разбивает длинные сообщения автоматически.

```bash
pip install requests
```

Настройка:
1. @BotFather → /newbot → копируешь токен
2. Пишешь боту что угодно
3. Открываешь `https://api.telegram.org/bot<TOKEN>/getUpdates` → берёшь chat_id

Запуск:
```bash
set TG_BOT_TOKEN=твой_токен
set TG_CHAT_ID=твой_chat_id
python 2_telegram_sender.py message.txt
```

Проверял на реальном боте — работает.

---

## 3. Архитектура

Подробно в `3_architecture.md`. Кратко:

- **1200 ящиков** = 12 доменов × 100 ящиков
- **Хостинг**: Zoho ($1/ящик) или Namecheap ($1.5/ящик)
- **Отправка**: Instantly.ai / Smartlead — там встроенный warmup и ротация
- **Стоимость**: ~$1,400/мес
- **Резерв**: 30% ящиков на замену выгоревших

Почему SaaS, а не своя инфра? Потому что на 1200 ящиков DevOps-затраты не окупятся. Своё имеет смысл от 5000+.

---

## Зависимости

```bash
pip install dnspython requests
```

---

Если есть вопросы — пишите.
