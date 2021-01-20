import os
from django.conf import settings
from ..utils import folder_utils


def getJobsList():
    jobs_list = os.listdir(settings.VIDEOS_DIR)
    return jobs_list


def createJob(name):
    folder_utils.checkJobFolder(name)
