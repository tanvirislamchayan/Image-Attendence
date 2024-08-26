from django.urls import path
from subjects import views



urlpatterns = [
    path('show-subjects/', views.show_subjects, name='subjects'),
    path('add-subjects-excel/', views.add_subjects, name='add_subjects_excel'),
    path('add-subject-demo/', views.add_subjects_demo, name='add_subject_demo')
]

