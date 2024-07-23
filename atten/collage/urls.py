from django.urls import path
from collage import views

urlpatterns = [
    path('collage-info/', views.collage_info, name = 'collage_info' ),
    path('add-collage/', views.add_collage, name = 'add_collage' ),
]