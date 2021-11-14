#!/bin/bash

GROUND_ZERO="/tmp/radioactive-waste"
NUMBERS="$GROUND_ZERO/numbers"
TETANUS="$GROUND_ZERO/rust-playground"

echo "Detonating..."
rm -rf $GROUND_ZERO
echo "$GROUND_ZERO has been eliminated."

echo "Deploying to $GROUND_ZERO"
mkdir -p $GROUND_ZERO

echo "Entering $GROUND_ZERO"
cd $GROUND_ZERO

echo "Populating $NUMBERS"

mkdir -p $NUMBERS
for i in {0..20}
do
    touch "$NUMBERS/$i"
    touch "$NUMBERS/$i.txt"
done

echo "Quarantine $TETANUS"
cargo new rust-playground
