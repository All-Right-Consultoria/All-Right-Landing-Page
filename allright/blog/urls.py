from django.contrib import admin
from django.urls import include, path
from .views import LandingPage


urlpatterns = [
    path('', LandingPage),
]

