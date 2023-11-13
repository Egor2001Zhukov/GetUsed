import os

import requests
from celery import shared_task
from dotenv import load_dotenv

from app.models import Habit

load_dotenv()


@shared_task()
def send_telegram_notification(**kwargs):
    try:
        habit_id = kwargs.get('habit_id')
        habit = Habit.objects.filter(id=habit_id).first()
        message = f'Мне сейчас нужно совершить действие - {habit.action}. Место - {habit.place}'
        requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('GET_USED_TELEGRAM_BOT_TOKEN')}/sendMessage",
            data={'chat_id': habit.user.chat_id_telegram, 'text': message})
        return 'OK'
    except Exception as e:
        return f'ERROR({e})'
