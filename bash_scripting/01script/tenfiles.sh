#!/bin/bash

# Pick a random number to folder
RANDOMFOLDER=$((1 + $RANDOM % 10))

# If folder exists, delete
if [ -d "${RANDOMFOLDER}" ]; then
    rm -rf $RANDOMFOLDER
fi

# Create the folder
mkdir $RANDOMFOLDER

# Create ten files
for NEWFILE in $(seq 10)
do
    echo "New file in : $RANDOMFOLDER/$NEWFILE.txt"
    echo $(date) > "$RANDOMFOLDER/$NEWFILE.txt"
done
