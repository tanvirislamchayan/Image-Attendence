from django.urls import path
from students import views


urlpatterns = [
    path('student-attendence/', views.show_students, name='attendence'),
    path('add-students/', views.add_students, name='add_student'),
    path('add-date/', views.add_dates, name='add_dates'),
    path('download-demo-excel/', views.download_demo_excel, name='download_demo_excel'),
    # path('present', views.present, name='present')
]