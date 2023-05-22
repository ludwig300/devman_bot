import logging
import os
import time

import requests
from dotenv import load_dotenv
from telegram import Bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Devman Bot")


def get_new_attempts(token, timestamp=None):
    dvmn_url = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {token}",
    }
    params = {
        "timestamp": timestamp,
    }
    response = requests.get(dvmn_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()

    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    dvmn_api_token = os.environ['DVMN_API_TOKEN']

    bot = Bot(token=tg_token)
    last_timestamp = None

    while True:
        try:
            logger.info("Making request to Devman API...")
            attempts = get_new_attempts(dvmn_api_token, last_timestamp)
            logger.info("Got response from Devman API.")

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

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            logger.exception("An error occurred while making request to Devman API.")
            time.sleep(600)
        except Exception as e:
            logger.exception("An unexpected error occurred.")
            break


if __name__ == "__main__":
    main()
