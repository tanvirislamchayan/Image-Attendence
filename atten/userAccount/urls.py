from django.urls import path
from userAccount import views



urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('users/', views.users, name='users')
]

