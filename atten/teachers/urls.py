from django.urls import path
from teachers import views


urlpatterns = [
    path('', views.teachers_info, name='teachers'),
]