from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.Home.as_view(), name="search" ),
]
