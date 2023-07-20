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


## Запуск с помощью Docker

1. Убедитесь, что у вас установлен Docker. Если нет, скачайте его [здесь](https://www.docker.com/products/docker-desktop) и установите.
2. Создайте образ Docker из Dockerfile, который находится в корневом каталоге проекта. В командной строке перейдите в каталог проекта и выполните следующую команду (не забудьте заменить `your_image_name` на имя, которое вы хотите дать образу):

```bash
>docker build -t your_image_name .
```

3. Запустите контейнер Docker из созданного образа. Вместо `your_image_name` используйте имя, которое вы дали образу, а вместо `your_container_name` используйте имя, которое вы хотите дать контейнеру:

```bash
>docker run -d --name your_container_name --env-file .env your_image_name
```

Заметьте, что `--env-file .env` указывает Docker на файл, из которого следует брать переменные окружения. Вместо `.env` укажите путь к вашему файлу с переменными окружения.

Теперь бот запущен внутри Docker контейнера и будет отправлять вам уведомления в Telegram каждый раз, когда ваше задание на Devman будет проверено.

Если вам нужно остановить контейнер Docker, вы можете сделать это с помощью следующей команды:

```bash
>docker stop your_container_name
```

Где `your_container_name` - это имя, которое вы дали контейнеру при его создании.
