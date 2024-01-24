from django.contrib import admin
from django.urls import path
from .views import LandingPageView, AboutPageView, CaseListView


urlpatterns = [
    path('', LandingPageView),
    path('about/', AboutPageView),
    path('cases/', CaseListView.as_view(), name='cases-list'),
    # path('posts/', PostListView), # TODO: A ser implementado futuramente
]

