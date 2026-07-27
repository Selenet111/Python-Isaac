from pydub import AudioSegment
from pydub.playback import play

import os
ffmpegpath = r"C:\Users\isaac\Downloads\ffmpeg\bin"
os.environ["PATH"] += os.pathsep + ffmpegpath


song = AudioSegment.from_file(r"holdingnothingback.mp3", format = "mp3")

#https://github.com/jiaaro/pydub

play(song)