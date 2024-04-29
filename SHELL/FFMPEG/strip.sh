#!/bin/bash

# strip.sh: - akin to python strip()

TRIM_TIME="2.5"

# Check if a directory is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 [DIRECTORY]"
    exit 1
fi

# Check if the directory exists
if [ ! -d "$1" ]; then
    echo "$(basename -- $0): Directory '$1' not found"
    exit 1
fi

SAVEDIR="$PWD/$(basename -- $1)-strip"
rm -rf "$SAVEDIR"
mkdir -p "$SAVEDIR"

# List of acceptable video MIME types
acceptable_types=("video/mp4" "video/quicktime" "video/x-msvideo" "video/x-flv" "video/x-matroska" "video/webm" "video/x-ms-wmv")

# Loop through each file in the directory
for file in "$1"/*; do
    if [ -f "$file" ]; then
        # Get the MIME type of the file
        mime_type=$(file -b --mime-type "$file")

        # Check if the MIME type is in the list of acceptable types
        if [[ " ${acceptable_types[@]} " =~ " $mime_type " ]]; then
            echo "Processing file: $file"
            filename=$(basename -- "$file")
            extension="${filename##*.}"
            filename="${filename%.*}"

            # Use ffprobe to get the duration of the video
            duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file")

            # Calculate the new duration
            double_trim_time=$(echo "$TRIM_TIME * 2" | bc -l)
            new_duration=$(echo "$duration - $double_trim_time" | bc -l)

            # Use ffmpeg to strip the video
            ffmpeg -ss $TRIM_TIME -t "$new_duration" -i "$file" -c copy "$SAVEDIR/$filename-stripped.$extension" -loglevel error

            echo "Stripped file saved as: $SAVEDIR/$filename-stripped.$extension"
        else
            echo "Skipping file: $file (unsupported format)"
        fi
    fi
done
