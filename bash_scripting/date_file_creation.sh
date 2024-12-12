#!/usr/bin/env bash

#no input provided check
if [ $# -eq 0 ]; then
    echo "Error: please provide the name of the directory as an input"
    echo "Script Usage: $0 <folder_name>"
    exit 1
fi

#gate name of the directory
dir_name="$1"

#check if directory already exists
if [ -d "$dir_name" ]; then
    echo "Directory '$dir_name' already exists, deleting it..."
    #remove directory
    rm -rf "$dir_name"
fi

#creating new directory 
echo "creating new '$dir_name' directory"
mkdir "$dir_name"
echo "directory '$dir_name' has been created"

#accessing directory
echo "accessing '$dir_name' ..."
cd "$dir_name"

#creating 10 files and adding timestamp
echo "creating 10 files with timestamp each second"
for i in {1..10} 
do 
    # Get the current timestamp
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    echo "File created on: $timestamp" > "$i.txt"
    # Wait for 1 second before the next iteration
    sleep 1
done
echo "files created"