from django.urls import path
from teachers import views


urlpatterns = [
    path('teachers-info/', views.teachers_info, name='teachers'),
    path('login/', views.user_login, name='login'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('teacher-details/<str:uid>/', views.teacher_detail,  name='teachers_detail'),
    path('upload-profile-image', views.upload_profile, name='upload_profile'),
    path('upload-routine', views.upload_routine, name='upload_routine'),
    path('logout-user', views.logout_user, name='logout_user')
    # path('user-login/', views.login_user, name='user_login')
]