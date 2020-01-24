from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv
from datetime import datetime

#get date

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Download data and config
download_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

# Song Directory
if not os.path.exists('Songs'):
	os.mkdir('Songs'),
	os.chdir('Songs')
else:
	os.chdir('Songs')

log=[]

# Download Songs
with youtube_dl.YoutubeDL(download_options) as dl:
	with open('../songs.txt' ,'r') as f:
		for song_url in f:
			dl.download([song_url])

open('../songs.txt', 'w').close()