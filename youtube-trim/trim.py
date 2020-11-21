import os
import subprocess
from subprocess import PIPE

from rich.progress import track

BASE_DIR = os.getcwd()
SONG_DIR = os.path.join(os.getcwd(), 'Songs')
SAVE_DIR = os.path.join(os.getcwd(), 'Trimmed')

PLAYLIST_ID = "PLAYLIST ID"

os.chdir(SONG_DIR)

# Downloading Songs
print('Downloading Playlist...')
subprocess.run(['youtube-dl', '-x', '--audio-format', 'mp3', '-i', PLAYLIST_ID])

os.chdir(BASE_DIR)

songs = os.listdir(SONG_DIR)

for song in track(songs, description='Trimming Songs'):
    subprocess.run(['sox', f'{SONG_DIR}/{song}', f'{SAVE_DIR}/{song}', 'silence', '1', '0.1', '1%', '-1', '0.5', '1%'])
