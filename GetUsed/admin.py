from django.contrib import admin

from GetUsed import models


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('minute', 'hour', 'day', 'user')


@admin.register(models.Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'user')
