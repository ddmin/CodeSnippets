#!/bin/bash

GROUND_ZERO="/tmp/nuclear-fallout"
NUMBERS="$GROUND_ZERO/numbers"
WORDS="$GROUND_ZERO/words"
TETANUS="$GROUND_ZERO/rust-playground"

echo "Detonating..."
rm -rf $GROUND_ZERO

cat << "EOF"
                         ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
EOF

echo "$GROUND_ZERO has been eliminated."

echo "Deploying to $GROUND_ZERO"
mkdir -p $GROUND_ZERO

echo "Entering $GROUND_ZERO"
cd $GROUND_ZERO

echo "Populating $NUMBERS"

mkdir -p $NUMBERS
for i in {0..20}
do
    mkdir "$NUMBERS/$i-dir"
    touch "$NUMBERS/$i-file"
    touch "$NUMBERS/$i-text.txt"
done

echo "Prophecy of $WORDS"

mkdir -p $WORDS
for i in {0..30}
do
    for x in {0..10}
    do
        openssl rand -hex 20 >> "$WORDS/$i.txt"
    done
done

echo "Quarantine $TETANUS"
cargo new rust-playground
