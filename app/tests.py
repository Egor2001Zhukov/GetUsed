from datetime import timedelta

from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from app import models
from users.models import User


class HabitAPITestCase(APITestCase):
    """Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.
    Сохраните результат проверки покрытия тестами."""

    def setUp(self):
        self.user = User.objects.create_user(email='testemail@gmail.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.schedule = models.Schedule.objects.create(minute=[23], hour=[21], day=[], user=self.user)
        self.habit = models.Habit.objects.create(place='Улица', action='Пойти прогуляться', schedule=self.schedule,
                                                 time_to_complete=timedelta(seconds=12), is_public=True, user=self.user)

    def test_post(self):
        # Тестирование POST-запроса к API
        response = self.client.post('http://127.0.0.1:8000/api/my_habits/',
                                    data={'place': 'Улица', 'action': 'Пойти прогуляться', 'schedule': self.schedule.id,
                                          'time_to_complete': 12, 'is_public': True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        # Тестирование GET-запроса к API
        response = self.client.get(f'http://127.0.0.1:8000/api/my_habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get(self):
        # Тестирование GET-запроса к API
        response = self.client.get(f'http://127.0.0.1:8000/api/my_habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        # Тестирование POST-запроса к API
        response = self.client.put(f'http://127.0.0.1:8000/api/my_habits/{self.habit.id}/',
                                   data={'place': 'Дома', 'action': 'Почитать книгу', 'schedule': self.schedule.id,
                                         'time_to_complete': timedelta(seconds=12), 'is_public': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        # Тестирование POST-запроса к API
        response = self.client.delete(f'http://127.0.0.1:8000/api/my_habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_public_list(self):
        # Тестирование GET-запроса к API
        response = self.client.get(reverse_lazy('GetUsed:public_habit'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ScheduleAPITestCase(APITestCase):
    """Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.
    Сохраните результат проверки покрытия тестами."""

    def setUp(self):
        self.user = User.objects.create_user(email='testemail@gmail.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.schedule = models.Schedule.objects.create(minute=[23], hour=[21], day=[], user=self.user)

    def test_post(self):
        # Тестирование POST-запроса к API
        response = self.client.post('http://127.0.0.1:8000/api/my_schedules/',
                                    data={"minute": [23], "hour": [21], "day": []})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        # Тестирование GET-запроса к API
        response = self.client.get(f'http://127.0.0.1:8000/api/my_schedules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get(self):
        # Тестирование GET-запроса к API
        response = self.client.get(f'http://127.0.0.1:8000/api/my_schedules/{self.schedule.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        # Тестирование POST-запроса к API
        response = self.client.put(f'http://127.0.0.1:8000/api/my_schedules/{self.schedule.id}/',
                                   data={"minute": [31], "hour": [20], "day": []})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        # Тестирование POST-запроса к API
        response = self.client.delete(f'http://127.0.0.1:8000/api/my_schedules/{self.schedule.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
