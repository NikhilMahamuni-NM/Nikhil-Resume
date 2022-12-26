from django.urls import path

from . import views

APP_NAME = "cv"

urlpatterns = [
    path('', views.home, name="home"),
	
]
