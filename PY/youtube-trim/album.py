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
        subprocess.run(['id3v2', '-A', ALBUM_NAME, song])

    except:
        pass
