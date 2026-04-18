from django.urls import path

from staff import views

urlpatterns = [
    path('', views.staffindex)
]