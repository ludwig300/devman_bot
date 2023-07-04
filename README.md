# Devman Bot

Проект представляет собой телеграм-бота, который отправляет уведомления о проверке заданий на [Devman](https://dvmn.org/).

## Установка

1. Клонируйте репозиторий с проектом:

```bash
>git clone git@github.com:ludwig300/devman_bot.git
```

2. Создайте и активируйте виртуальное окружение:

```bash
>python3 -m venv venv
>source venv/bin/activate
```

3. Установите необходимые зависимости:

```bash
>pip install -r requirements.txt
```

## Настройка

1. Создайте файл `.env` в корневом каталоге проекта.
2. Добавьте в файл `.env` следующие строки, заменив `your_value` на соответствующие значения:

```
TG_TOKEN=your_value
LOGGING_BOT_TOKEN=your_value
TG_CHAT_ID=your_value
DVMN_API_TOKEN=your_value
```

`TG_TOKEN`  и `LOGGING_BOT_TOKEN` - это токены ваших ботов в Telegram, `TG_CHAT_ID `- идентификатор вашего чата в Telegram,

`DVMN_API_TOKEN` - это токен вашего аккаунта на Devman.

## Запуск

Чтобы запустить бота, выполните следующую команду:

```bash
>python main.py
```

Теперь бот будет отправлять вам уведомления в Telegram каждый раз, когда ваше задание на Devman будет проверено.
