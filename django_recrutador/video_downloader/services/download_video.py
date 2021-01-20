import urllib.request as urllib
import os
from django.conf import settings


def testDownload():
    url = 'https://storage-matchboxbrasil.sfo2.digitaloceanspaces.com/production/uploads' \
          '/3593deac1f33a7b7c856fb4ae3895614.webm '
    file_name = 'test_video.webm'
    full_file_name = os.path.join(settings.VIDEOS_DIR, 'TestJob', file_name)

    checkVideosFolder()

    folder_exists = os.path.exists(os.path.join(settings.VIDEOS_DIR, 'TestJob'))
    if not folder_exists:
        os.mkdir(os.path.join(settings.VIDEOS_DIR, 'TestJob'))

    urllib.urlretrieve(url, full_file_name)
    return full_file_name


def checkVideosFolder():
    folder_exists = os.path.exists(settings.VIDEOS_DIR)
    if not folder_exists:
        os.mkdir(settings.VIDEOS_DIR)
