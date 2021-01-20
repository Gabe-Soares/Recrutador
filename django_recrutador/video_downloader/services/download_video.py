import urllib.request as urllib


def testDownload(url, file):
    urllib.urlretrieve(url, file)
    return
