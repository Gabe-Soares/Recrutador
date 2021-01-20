from django.urls import path, include

urlpatterns = [
    path('testDownload/', include('video_downloader.urls')),
]
