from django.urls import path
from students import views


urlpatterns = [
    path('student-attendence/', views.show_students, name='attendence'),
    path('add-date/', views.add_dates, name='add_dates'),
    # path('present', views.present, name='present')
]