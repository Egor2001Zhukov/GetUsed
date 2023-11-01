from rest_framework import serializers


class ExclusionOfRemunerationValidator:
    def __call__(self, habit):
        if habit.reward and habit.is_pleasant:
            raise serializers.ValidationError('Привычка не может одновременно быть приятной и вознаграждаться')


class TimeToCompleteValidator:
    def __call__(self, habit):
        if habit.time_to_complete.total_seconds() > 120:
            raise serializers.ValidationError('Привычка не может занимать более 120 секунд')


class RelatedHabitsValidator:
    def __call__(self, habit):
        related_habit = habit.related_habit
        if related_habit:
            if related_habit.is_pleasant is False:
                raise serializers.ValidationError('Связанная привычка должна быть приятной')


class PleasantHabitsValidator:
    def __call__(self, habit):
        if habit.is_pleasant:
            if habit.related_habit or habit.reward:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки.')


class ScheduleValidator:
    def __call__(self, schedule):
        error = ''
        for minute in schedule.minute:
            if 0 > minute or minute > 59:
                error += 'Минуты должны быть в диапазоне 0 - 59. '
                break
        if schedule.hour:
            for hour in schedule.hour:
                if 0 > hour or hour > 23:
                    error += 'Часы должны быть в диапазоне 0 - 23. '
                    break
        if schedule.day:
            for day in schedule.day:
                if 0 > day or day > 6:
                    error += 'Дни должны быть в диапазоне 0 - 6 (0 - воскресенье). '
                    break
        if error:
            raise serializers.ValidationError(error[:-1])


habit_validators = [ExclusionOfRemunerationValidator, TimeToCompleteValidator, RelatedHabitsValidator,
                    PleasantHabitsValidator]
