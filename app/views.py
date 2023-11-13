from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app import models, serializers, pagination, services
from app.permissions import IsOwner


class UserHabitApiViewSet(ModelViewSet):
    serializer_class = serializers.HabitSerializer
    pagination_class = pagination.HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return models.Habit.objects.filter(user=self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        services.create_habit_task(habit.id)

    # def perform_destroy(self, instance):


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = serializers.HabitSerializer

    def get_queryset(self):
        return models.Habit.objects.filter(is_public=True).order_by('created_at')


class UserScheduleApiViewSet(ModelViewSet):
    serializer_class = serializers.ScheduleSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return models.Schedule.objects.filter(user=self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def health(request):
    return JsonResponse({"status": "ok"})
