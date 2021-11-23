#!/bin/bash

set -e

# Directory of Egress
EGRESS="$HOME/.local/hide"
mkdir -p $EGRESS

# directories to move
dirs=("Code" "Desktop" "Documents" "Downloads" "Music" "Pictures" "Public" "Templates" "Videos" "VirtualBox")

# loop through directories
for d in ${dirs[@]}; do

    if [ "$1" == "reset" ]; then
        mv "$EGRESS/$d" "$HOME/$d"
    else
        mv "$HOME/$d" "$EGRESS/$d"
    fi

done
