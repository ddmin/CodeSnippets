#!/bin/bash

set -e

# Directory of Egress
EGRESS="$HOME/.local/hide"
mkdir -p $EGRESS

# directories to move
dirs=("Code" "Documents" "Downloads" "Music" "Pictures" "Public" "Templates" "Videos" "VirtualBox")

# loop through directories
for d in ${dirs[@]}; do

    if [ "$1" == "reset" ]; then
        [ -d "$HOME/$d" ] && echo "$HOME/$d already exists." && echo "Try removing \`reset\`." && exit
        mv "$EGRESS/$d" "$HOME/$d"
    else
        [ -d "$EGRESS/$d" ] && echo "$EGRESS/$d already exists." && echo "Try adding \`reset\`." && exit
        mv "$HOME/$d" "$EGRESS/$d"
    fi

done
