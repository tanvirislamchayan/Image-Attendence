from django.urls import path
from teachers import views


urlpatterns = [
    path('', views.teachers_info, name='teachers'),
    path('login/', views.user_login, name='login'),
    path('add-user/', views.add_user, name='add_user'),
    path('teacher-details/<str:uid>/', views.teacher_detail,  name='teachers_detail'),
    path('upload-profile-image', views.upload_profile, name='upload_profile'),
    path('upload-routine', views.upload_routine, name='upload_routine')
]