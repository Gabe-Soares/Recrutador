import os
from django.conf import settings


def checkVideosFolder():
    folder_exists = os.path.exists(settings.VIDEOS_DIR)
    if not folder_exists:
        os.mkdir(settings.VIDEOS_DIR)


def checkJobFolder(job_name):
    folder_exists = os.path.exists(os.path.join(settings.VIDEOS_DIR, job_name))
    if not folder_exists:
        os.mkdir(os.path.join(settings.VIDEOS_DIR, job_name))
