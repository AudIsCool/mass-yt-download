#Youtubedl
from os import link
import youtube_dl

#get texts
linkList = []

with open("links.txt") as file: 
    text = file.read()
    linkList = text.split("\n")

#Setup youtube dl 
def downloadHook(info):
    if info["status"] == "finished":
        print("Done downloading")

#Setup for audio quality
ydlOptions = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [downloadHook],
    'outtmpl': './downloadFolder/%(title)s.%(ext)s'
}

youtubedl = youtube_dl.YoutubeDL(ydlOptions)

#Download each
youtubedl.download(linkList)