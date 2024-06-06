#!/bin/bash
# redlib: read reddit bmk file and return subscriptions in RedLib format

set -e

# REDLIB INSTANCES
SITE=(
    ""
    "https://l.opnxng.com"
    "https://libreddit.bus-hit.me"
    "https://reddit.idevicehacked.com"
    "https://redlib.catsarch.com"
    "https://redlib.freedit.eu"
    "https://redlib.perennialte.ch"
    "https://redlib.tux.pizza"
    "https://rl.bloat.cat"
)

# https://stackoverflow.com/a/28326129
choose ()
{
    select INST; do
        if [ 1 -le "$REPLY" ] && [ "$REPLY" -le $# ]; then
            break;
        else
            >&2 echo
            >&2 echo "Invalid Input: Select a number 1-$#"
        fi
    done
}

usage() {
    >&2 echo
    >&2 echo "USAGE: $(basename "$0") [SUBREDDITS.BMK]"
    >&2 echo "SUBREDDIT FORMAT: @/r/SubredditName"
}

# check if at least one argument
if [ $# -lt 1 ]; then
    >&2 echo "ERROR: please provide a subreddit.bmk file"
    usage
    exit 1
fi

# check if file exists
if [ ! -f "${1}" ]; then
    >&2 echo "ERROR: file '${1}' doesn't exist."
    usage
    exit 1
fi

# read links from bmk
subreddits=$(cat ${1} | grep -e '^@/r/' | sed 's/^@\/r\///')

# choose RedLib instance
choose "${SITE[@]}"

# base URL with settings
URL="${INST}/settings/restore/?theme=gruvboxdark&front_page=default&layout=card&wide=on&post_sort=hot&comment_sort=confidence&show_nsfw=on&use_hls=on&hide_hls_notification=off&hide_awards=off&fixed_navbar=on&filters%3d&subscriptions="

# separator for subreddits
SEPR="%2B"

for subreddit in $subreddits; do
    URL="${URL}${subreddit}${SEPR}"
done

# display formatted URL
echo $URL
