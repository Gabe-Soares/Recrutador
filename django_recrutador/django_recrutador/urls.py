from django.urls import path, include

urlpatterns = [
    path('', include('video_downloader.urls')),
]
