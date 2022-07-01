from os import link
from pytube import YouTube

link = "https://www.youtube.com/watch?v=9wh9mUum7vo"
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# videos=youtube_1.streams.filter(only_audio=True) #ONLY AUDIO

# videos = youtube_1.streams.all()
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)

# strm = int(input("Enter: "))
# videos[strm].download()
# print("Successfully Download")

# ***** Playlist Download *****

from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PLC3y8-rFHvwgg3vaYJgHGnModB54rxOk3")
print(f'Downloading: {py.title}')

for video in py.videos:
    video.streams.filter(res="720p").first().download()