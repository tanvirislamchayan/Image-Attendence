from django.urls import path
from departments import views


urlpatterns = [
    path('', views.departments, name='departments'),
    path('create/', views.create_dep, name='create_dep'),
    path('add-image/', views.add_img, name='update_department_image'),
]