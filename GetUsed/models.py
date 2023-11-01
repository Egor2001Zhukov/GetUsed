from django.db import models
from django.contrib.postgres.fields.array import ArrayField
from GetUsed import validators
from users.models import User


class Schedule(models.Model):
    minute = ArrayField(models.IntegerField(), verbose_name='Минуты')
    hour = ArrayField(models.IntegerField(), verbose_name='Часы', blank=True, null=True)
    day = ArrayField(models.IntegerField(), verbose_name='Дни недели', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.minute}_{self.hour}_{self.day}'

    def save(self, *args, **kwargs):
        schedule_validator = validators.ScheduleValidator()
        schedule_validator(self)
        super(Schedule, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = 'Расписания'


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name='Место')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', default=False)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name='Связанная привычка')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE,
                                 verbose_name='Расписание')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', blank=True, null=True)
    time_to_complete = models.DurationField(verbose_name='Время для выполнения')
    is_public = models.BooleanField(verbose_name='Публичность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.action

    def save(self, *args, **kwargs):
        for validator in validators.habit_validators:
            validator_obj = validator()
            validator_obj(self)
        super(Habit, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
