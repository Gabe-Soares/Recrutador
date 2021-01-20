from django.urls import path

from . import views

urlpatterns = [
    path('', views.testDownload, name='test'),
]