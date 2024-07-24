from django.urls import path
from home import views


urlpatterns = [
    path('', views.homa_page, name='home'),
]