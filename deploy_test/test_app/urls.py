from django.contrib import admin
from django.urls import path, include
from test_app import views

app_name = "test_app"

urlpatterns = [
    path("", views.main_view, name="main"),
]
