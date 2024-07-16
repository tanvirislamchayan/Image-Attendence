from django.urls import path
from departments import views


urlpatterns = [
    path('', views.departmets, name='departments'),
]