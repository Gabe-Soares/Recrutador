from django.http import HttpResponse
from .services import download_video


def download(request):
    if request.method == 'GET':
        result = download_video.testDownload()
        return HttpResponse(result)
