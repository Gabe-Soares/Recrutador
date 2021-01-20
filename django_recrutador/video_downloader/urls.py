from django.urls import path

from . import views

urlpatterns = [
    path('testDownload/', views.testDownload, name='test'),
    path('', views.home, name='home'),
]