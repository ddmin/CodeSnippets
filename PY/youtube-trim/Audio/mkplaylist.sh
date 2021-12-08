#!/bin/bash

MUSIC="$HOME/Music"
PLAYLIST="Anime.m3u"
ls -1 $MUSIC > "$HOME/.mpd/playlists/$PLAYLIST"
