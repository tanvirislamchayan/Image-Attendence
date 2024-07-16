from django.urls import path
from students import views


urlpatterns = [
    path('', views.show_students, name='students'),
]