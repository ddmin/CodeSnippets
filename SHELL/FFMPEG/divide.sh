#!/bin/bash

# divide.sh: Divide video into '$num_sections' sections, each '$section_duration' long

num_sections=10
section_duration=30

savedir="$PWD/div"
rm -rf "$savedir"
mkdir -p "$savedir"

# Check if a video file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 [VIDEO]"
    exit 1
fi

# Check if the video file exists
if [ ! -f "$1" ]; then
    echo "$(basename -- $0): File '$1' not found"
    exit 1
fi

# Get the base filename without extension
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"

# Use ffprobe to get the duration of the video
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1")

# Calculate the number of sections
total_duration=$(echo "$num_sections * $section_duration" | bc)

# Check if the video is long enough
if (( $(echo "$duration < $total_duration" | bc -l) )); then
    echo "$(basename -- $0): Video duration is less than $total_duration seconds ($num_sections sections of $section_duration seconds each)"
    exit 1
fi

for (( i=0; i<$num_sections; i++ )); do
    start_time=$(echo "$i * $section_duration" | bc -l)
    end_time=$(echo "($i + 1) * $section_duration" | bc -l)
    ffmpeg -i "$1" -ss "$start_time" -t "$section_duration" -c copy "$savedir/$filename-section-$i.$extension"
    echo "Section $i created: $filename-section-$i.$extension"
done
