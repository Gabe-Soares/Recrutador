from .controllers import videos_controller, job_controller
from django.shortcuts import render


def testDownload(request):
    if request.method == 'GET':
        videos_controller.testDownload()
        return render(request, 'testDownload.html', {})


def home(request):
    if request.method == 'GET':
        jobs_list = job_controller.getJobs()
        return render(request, 'index.html', {'jobs': jobs_list})
