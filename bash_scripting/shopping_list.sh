#!/usr/bin/env bash

# File to store the shopping list
list_file="shopping_list.txt"

echo "Would you like to create a new shopping list or add to the existing one?"
echo "Type 'new' to create a new list or 'add' to add to the existing list:"

# Read the user's choice
read -p "Your choice: " choice

# Process the user's choice
if [ "$choice" == "new" ]; then
    # Initialize an empty shopping list if the user wants a new list
    declare -a shopping_list=()
    echo "Creating a new shopping list..."
elif [ "$choice" == "add" ]; then
    # Load the existing shopping list from file, if available
    if [ -f "$list_file" ]; then
        IFS=$'\n' read -d '' -r -a shopping_list < "$list_file"
        echo "Loaded existing shopping list."
    else
        # Handle case where no existing list is found
        echo "No existing shopping list found. Starting a new list."
        declare -a shopping_list=()
    fi
else
    # Handle invalid user input
    echo "Invalid option. Please restart the script and choose 'new' or 'add'."
    exit 1
fi

# Prompt user to enter items for the shopping list
echo "Enter the items you want to add (type 'done' without quotes when finished):"

# Loop to read items from the user
while true; do
    read -p "Item to buy: " item
    if [ "$item" == "done" ]; then
        break
    fi
    
    # Check if the item is already in the list
    if [[ " ${shopping_list[*]} " == *" $item "* ]]; then
        echo "The item '$item' is already in the list."
    else
        # Append the new item to the shopping list
        shopping_list+=("$item")
        echo "Added '$item' to the list."
    fi
done

# Save the updated shopping list to the file, with each item on a new line
printf "%s\n" "${shopping_list[@]}" > "$list_file"

# Notify user that the list has been saved
echo "Your shopping list has been saved to $list_file."
