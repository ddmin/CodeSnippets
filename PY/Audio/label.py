import re
import subprocess
import os
from os.path import exists

ARTDIR="./Art"
SONGDIR="./Music"
PROCDIR="./proc"

EXCLUDE=[
    "Anohana",
    "Dr. Stone",
    "Nanatsu no Taizai",
    "Neon Genesis Evangelion",
    "Shingeki no Kyojin",
    "Sword Art Online",
    "Tokyo Ghoul",
]

if not exists(PROCDIR):
    os.mkdir(PROCDIR)

for file in os.listdir(SONGDIR):

    album = re.search("\[(.*)\]", file).group(1)

    if album in EXCLUDE:
        subprocess.run(['cp', f'{SONGDIR}/{file}', f'{PROCDIR}/{file}'])
        continue

    if exists(f'./Art/{album}.jpg'):
        art = f'./Art/{album}.jpg'
    elif exists(f'./Art/{album}.png'):
        art = f'./Art/{album}.png'
    else:
        art = 'Art/default.jpg'

    subprocess.run(
        [
            'id3v2',
            '-A', album,
            f'{SONGDIR}/{file}',
        ]
    )

    subprocess.run(
        [
            'ffmpeg',
            '-i', f'{SONGDIR}/{file}',
            '-i', art,
            '-map_metadata', '0',
            '-map', '0',
            '-map', '1',
            '-acodec', 'copy',
            file+'.mp3',
        ]
    )

    subprocess.run(['mv', file+'.mp3', f'{PROCDIR}/{file}'])
    print('='*60)
