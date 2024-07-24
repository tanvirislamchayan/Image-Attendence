from django.urls import path
from collages import views

urlpatterns = [
    path('collage-info/', views.collage_info, name = 'collage_info' ),
    path('add-collage/', views.add_collage, name = 'add_collage' ),
    path('create-collage/', views.create_collage, name='create_collage')
]