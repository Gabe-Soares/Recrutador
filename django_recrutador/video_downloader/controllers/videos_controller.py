from ..services import download_video
import os
from django.conf import settings
from ..utils import folder_utils


def testDownload():
    job = 'TestJob'

    url = 'https://storage-matchboxbrasil.sfo2.digitaloceanspaces.com/production/uploads' \
          '/3593deac1f33a7b7c856fb4ae3895614.webm'

    file_name = 'test_video.webm'
    full_file_name = os.path.join(settings.VIDEOS_DIR, job, file_name)

    folder_utils.checkVideosFolder()
    folder_utils.checkJobFolder(job)

    download_video.testDownload(url, full_file_name)
    return
