from django.urls import path

from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name
urlpatterns = [
    path('auth/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserCreateView.as_view(), name='register'),

]
