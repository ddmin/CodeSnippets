#!/bin/bash
# Condensed Audio Tagger/Trimmer

DIRECTORY=""

BASE_TITLE=""
ARTIST=""
ALBUM=""
IMAGE=""

OUTPUT_DIR="./output"
mkdir -p "$OUTPUT_DIR"


COUNTER=1
for FILE in "$DIRECTORY"/*.mp3; do
    BASENAME=$(basename "$FILE" .mp3)

    OUTPUT_FILE="${OUTPUT_DIR}/${BASENAME}-condensed.mp3"

    TITLE="${BASE_TITLE} ${COUNTER}"

    ffmpeg -ss 00:00:00 \
           -i "$FILE" -i "$IMAGE" \
           -c:a copy -c:v copy \
           -map 0:0 -map 1:0 \
           -id3v2_version 3 \
           -metadata title="$TITLE" \
           -metadata artist="$ARTIST" \
           -metadata album="$ALBUM" \
           -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" \
           "$OUTPUT_FILE"

    echo "Processed $FILE -> $OUTPUT_FILE with Title: $TITLE"

    COUNTER=$((COUNTER + 1))
done

echo "All files have been processed."
