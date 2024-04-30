#!/bin/bash
# yt-dlp rename.sh: AKA whoops I did it again.
# I forgot:
#           -o "%(playlist_index)s - %(title)s.%(ext)s"

# make sure to rename any '/' in the filename / playlist.txt
# also remove  %s/[&\/":?\-']//g

# idk why it doesn't work with mp4
# it only mostly works - fill in the gaps manually 🤷

RED='\033[1;31m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
NC='\033[0m'

IFS=$'\n'

RENAME_DIR="./rename"
if [[ -d "$RENAME_DIR" ]]
then
    echo "ERROR: '$RENAME_DIR' already exists. Aborting."
    exit 1
fi

rm -rf "$RENAME_DIR"
mkdir -p "$RENAME_DIR"

file_list=`find . -maxdepth 1 -type f -name '*.webm'`
lines=$(cat ./playlist.txt | wc -l)
counter=0

for video in $(cat ./playlist.txt);
do
    counter=$((counter+1))

    video_s=$(echo "$video" | tr -dc '[:alnum:]\n\r')
    line_number=$( echo "$file_list" | tr -dc '[:alnum:]\n\r' | grep -n "$video_s" | grep -Eo '^[^:]+')
    file_name=$(echo "$file_list" | awk 'NR == n' n=$line_number)

    if [[ -z "$line_number" ]];
    then
        echo -e "${WHITE}${counter}${NC}. ${RED}ERROR: '$video'${NC}"
        echo
        continue
    fi

    file_name=$(basename $file_name)
    new_name="${counter} - ${file_name}"

    cp "$file_name" "$RENAME_DIR/$new_name"
    echo -e "${WHITE}${counter}${NC}. ${GREEN}${file_name}${NC} ${WHITE}->${NC} ${CYAN}${new_name}${NC}"
    echo
done

unset IFS
