from django.urls import path
from rest_framework.routers import DefaultRouter

from app import views
from app.apps import GetusedConfig

app_name = GetusedConfig.name

router = DefaultRouter()
router.register(r'my_habits', views.UserHabitApiViewSet, basename='user_habits')
router.register(r'my_schedules', views.UserScheduleApiViewSet, basename='user_schedules')

urlpatterns = [
                  path('public_habit/', views.PublicHabitListAPIView.as_view(), name='public_habit'),
                  path('health', views.health)
              ] + router.urls
