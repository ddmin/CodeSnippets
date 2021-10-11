# Dependencies: ffmpeg, yt-dlp

from os.path import exists
import subprocess
import eyed3

with open('songs.conf', 'r') as f:
    songs = f.read().split('\n')[:-1]

songs = list(filter(lambda x: x, songs))
songs = list(filter(lambda x: x[0] != '#', songs))

for song in songs:
    vals = song.split(',')
    print(f'Link: {vals[0]}')
    print(f'Name: {vals[1]}')
    print(f'Artist: {vals[2]}')
    print(f'Album: {vals[3]}')
    print(f'Time: {vals[4]}')
    print('='*60)

    to_trim = False

    try:
        times = vals[4].split('-')
        start_time = times[0]
        end_time = times[1]
        to_trim = True
    except:
        pass

    subprocess.run(
        [
            'yt-dlp',
            '-x',
            '--audio-format', 'mp3',
            '-o', 'song.mp3',
            vals[0],
        ]
    )

    print('='*60)

    filename = f'[{vals[3]}] {vals[1]}'

    if to_trim:
        subprocess.run(
            [
                'ffmpeg',
                '-i', 'song.mp3',
                '-ss', f'{start_time}', '-to', f'{end_time}',
                'song2.mp3',
            ]
        )

        subprocess.run(['rm', 'song.mp3'])

        subprocess.run(['mv', 'song2.mp3', filename+'_pre.mp3'])

    else:

        subprocess.run(['mv', 'song.mp3', filename+'_pre.mp3'])

    if exists(f'./Art/{vals[3]}.jpg'):
        art = f'./Art/{vals[3]}.jpg'
    elif exists(f'./Art/{vals[3]}.png'):
        art = f'./Art/{vals[3]}.png'
    else:
        art = 'Art/default.jpg'

    subprocess.run(
        [
            'id3v2',
            '-t', vals[1],
            '-a', vals[2],
            '-A', vals[3],
            filename+'_pre.mp3',
        ]
    )

    subprocess.run(
        [
            'ffmpeg',
            '-i', filename+'_pre.mp3',
            '-i', art,
            '-map_metadata', '0',
            '-map', '0',
            '-map', '1',
            '-acodec', 'copy',
            filename+'.mp3',
        ]
    )

    subprocess.run(['rm', filename+'_pre.mp3'])

    print('='*60)
