# Тестовое задание — Polza Outreach Engine

## Структура

```
solution/
├── 1_email_checker.py    # Проверка MX-записей
├── 2_telegram_sender.py  # Отправка в Telegram
├── 3_architecture.md     # Архитектура аутрича
└── README.md             # Этот файл
```

---

## 1. Проверка email-доменов

### Установка
```bash
pip install dnspython
```

### Запуск
```bash
# Из файла (по одному email на строку)
python 1_email_checker.py emails.txt

# Через запятую
python 1_email_checker.py "test@gmail.com,user@yandex.ru,fake@notexist123.com"
```

### Пример вывода
```
test@gmail.com — домен валиден
fake@notexist12345.xyz — домен отсутствует
user@yandex.ru — домен валиден
```

---

## 2. Telegram отправка

### Установка
```bash
pip install requests
```

### Настройка
1. Создай бота: @BotFather → /newbot
2. Скопируй токен
3. Напиши боту любое сообщение
4. Открой `https://api.telegram.org/bot<TOKEN>/getUpdates` → найди chat_id

### Запуск
```bash
set TG_BOT_TOKEN=123456:ABC-DEF
set TG_CHAT_ID=123456789
python 2_telegram_sender.py message.txt
```

---

## 3. Архитектура

См. файл `3_architecture.md`

Краткое резюме:
- 12 доменов × 100 ящиков = 1200 email
- SaaS для отправки (Instantly.ai / Smartlead)
- Стоимость: ~$1,400/мес
- Резерв 30% на замену выгоревших

---

## Зависимости

```bash
pip install dnspython requests
```
