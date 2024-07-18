from django.urls import path
from students import views


urlpatterns = [
    path('', views.show_students, name='students'),
    path('add-date/', views.add_dates, name='add_dates'),
]