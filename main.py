import logging
import os
import time

import requests
from dotenv import load_dotenv
from telegram import Bot


logger = logging.getLogger("Devman Bot")


class TelegramHandler(logging.Handler):
    def __init__(self, tg_bot_token, chat_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = Bot(token=tg_bot_token)
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_new_attempts(token, timestamp=None):
    dvmn_url = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {token}",
    }
    params = {
        "timestamp": timestamp,
    }
    response = requests.get(
        dvmn_url,
        headers=headers,
        params=params,
        timeout=60
    )
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()

    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    dvmn_api_token = os.getenv('DVMN_API_TOKEN')

    bot = Bot(token=tg_token)

    logging_bot_token = os.getenv('LOGGING_BOT_TOKEN')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    tg_handler = TelegramHandler(logging_bot_token, tg_chat_id)
    tg_handler.setLevel(logging.INFO)
    tg_handler.setFormatter(formatter)

    logger.addHandler(tg_handler)

    last_timestamp = None
    logger.info("Бот запущен")
    while True:
        try:
            logger.debug("Making request to Devman API...")
            attempts = get_new_attempts(dvmn_api_token, last_timestamp)
            logger.debug("Received response from Devman API.")

            if attempts['status'] == 'found':
                new_attempts = attempts['new_attempts']
                for attempt in new_attempts:
                    is_negative = attempt['is_negative']
                    lesson_title = attempt['lesson_title']
                    lesson_url = attempt['lesson_url']
                    bot.send_message(
                        chat_id=tg_chat_id,
                        text=f"Урок '{lesson_title}' проверен. Результат: {'неудачно' if is_negative else 'успешно'}. Ссылка на урок {lesson_url}",
                    )
                    logger.info("Sent message to Telegram.")
                    last_timestamp = attempt['timestamp']
            else:
                last_timestamp = attempts['timestamp_to_request']

        except requests.exceptions.ReadTimeout:
            logger.debug("Read timeout occurred. The server did not respond in a timely manner. Retrying immediately")
        except requests.exceptions.ConnectionError:
            logger.warning("A connection error occurred. Please check the network connection. Retrying in 10 minutes...")
            time.sleep(600)
        except Exception:
            logger.exception("An unexpected error occurred.")


if __name__ == "__main__":
    main()
