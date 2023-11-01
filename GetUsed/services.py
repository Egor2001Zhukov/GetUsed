import json

from django.utils import timezone
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from GetUsed import models


def create_habit_task(habit_id):
    habit = models.Habit.objects.get(id=habit_id)
    schedule = habit.schedule
    minute = ','.join(schedule.minute) if len(schedule.minute) > 1 else schedule.minute[0]
    hour = ','.join(schedule.hour) if len(schedule.hour) > 1 else (schedule.hour[0] if schedule.hour else '*')
    day = ','.join(schedule.day) if len(schedule.day) > 1 else (schedule.day[0] if schedule.day else '*')

    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=minute,
        hour=hour,
        day_of_week=day,
        day_of_month="*",
        month_of_year="*",
        timezone="Europe/Moscow"
    )

    PeriodicTask.objects.create(
        name=f'habit{habit_id}',
        task='GetUsed.tasks.send_telegram_notification',
        crontab=crontab_schedule,
        kwargs=json.dumps({'habit_id': habit_id, }),
        start_time=timezone.now(),
    )
