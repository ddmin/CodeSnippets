#!/bin/bash

# add-subs.sh: add hardcoded subtitles

usage() {
    echo "Usage: $0 [VIDEO]"
}

if [[ -z $1 ]]; then
    echo "$0: Please provide an video file."
    usage
    exit
fi

ffmpeg -i "$1" -vf "subtitles=subtitles.srt" output.mp4
