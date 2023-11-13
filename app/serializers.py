from rest_framework import serializers

from app import models


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Habit
        fields = ['id', 'place', 'action', 'is_pleasant', 'related_habit', 'schedule', 'reward', 'time_to_complete',
                  'is_public']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = ['id', 'minute', 'hour', 'day']
