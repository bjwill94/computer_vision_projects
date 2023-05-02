# from pytube import YouTube as yt
# # yt = YouTube("https://www.youtube.com/watch?v=6iO3TSOC0ko")
# # yt = yt.get('mp4', '720p')
# # yt.download('C:/Users/HP/Desktop/videos')
#
# url = 'https://www.youtube.com/watch?v=6iO3TSOC0ko'
# # yt('url').streams.first().download('C:/Users/HP/Desktop/videos')
# yt(url).streams.first()
# yt.streams.filter(res="1080p").first().download()
from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

downloadYouTube('https://www.youtube.com/watch?v=u9weg02yGrk', 'C:/Users/HP/Desktop/videos')