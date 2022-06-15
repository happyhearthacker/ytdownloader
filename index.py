# pip install pytube

import pytube
link = input('URL please')
yt = pytube.Youtube(link)
yt.streams.first().download()
print('Downloading', link)
