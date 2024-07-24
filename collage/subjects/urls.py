from django.urls import path
from subjects import views



urlpatterns = [
    path('', views.show_subjects, name='subjects')
]

