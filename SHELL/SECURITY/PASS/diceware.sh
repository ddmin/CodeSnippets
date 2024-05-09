#!/bin/bash

set -e

RED='\033[1;31m'
NC='\033[0m'

usage() { echo "Usage: $(basename $0) [-n(umber of words)] [-v(erbose)] [-h(elp)] [FILE]"; }

dice() {
    local roll=$((1 + $RANDOM % 6))
    echo $roll
}

dice5() {
    roll=""
    for i in $(eval echo {1..$1});
    do
        roll="${roll}$(dice)"
    done
    echo $roll
}

diceware() {
    for x in $(eval echo {1..$3});
    do
        dw=$(dice5 $2)

        # verbose
        if [ "$4" -eq "1" ]; then
            echo -e "${RED}($dw)${NC}"
        fi

        word=$(grep -w "${dw}" $1 | sed -n '1p' | awk '{ print $2 }')
        echo $word
    done
}

verbose=0
help=0
while getopts ":hvn::" o; do
    case "${o}" in
        h)
            help=1
            ;;
        n)
            n=${OPTARG}
            ;;
        v)
            verbose=1
            ;;
        *)
            usage
            exit 1
            ;;
    esac
done
shift $((OPTIND-1))

file="${1}"

if [ ! -z ${n} ]; then
    case "${n}" in
        ''|*[!0-9]*) echo -e "${RED}ERROR: enter a positive '-n' value${NC}" 1>&2 ; usage; exit 1;;
        *) ;;
    esac
fi

howmany=$((n))

if [ "${help}" -eq "1" ]; then
    usage
    exit 0
fi

if [ -z "${file}" ]; then
    echo -e "${RED}ERROR: no file was provided${NC}" 1>&2
    usage
    exit 1
fi

if [ -z "${n}" ]; then
    howmany=7
fi

if [ $howmany -lt 1 ]; then
    echo -e "${RED}ERROR: enter a positive '-n' value${NC}" 1>&2
    usage
    exit 1
fi

if [ ! -f $file ]; then
    echo -e "${RED}ERROR: file '$file' does not exist${NC}" 1>&2
    usage
    exit 1
fi

length=$(cat $file | awk '{print $1}' | sed -n '1p' | wc -c)
length=$((length-1))
diceware $file $length $howmany $verbose | sed -rz 's/[\r\n]+/ /g' | sed 's/ $//'
