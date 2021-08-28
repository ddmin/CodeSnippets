import os
import subprocess
from subprocess import PIPE
import re

BASE_DIR = os.getcwd()
SONG_DIR = os.path.join(os.getcwd(), 'Songs')
SAVE_DIR = os.path.join(os.getcwd(), 'Trimmed')

ALBUM_NAME = "ALBUM NAME"

os.chdir(SAVE_DIR)
songs = os.listdir(SAVE_DIR)

for song in songs:
    try:
        if song[0] == "'":
            first_half, second_half = song.split('by')
            title = re.search(r"'(.*)'", first_half).group(1)
            title = title.strip()
            artist = re.search(r" (.*) 【", second_half).group(1)
            artist = artist.strip()

            subprocess.run(['mv', song, title+'.mp3'])
            subprocess.run(['id3v2', '-a', artist, title+'.mp3'])
            subprocess.run(['id3v2', '-t', title, title+'.mp3'])
            subprocess.run(['id3v2', '-A', ALBUM_NAME, title+'.mp3'])

        else:
            pass
    except:
        pass
