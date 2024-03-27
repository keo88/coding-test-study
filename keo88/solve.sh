#!/bin/bash

# Step 1: Take leetcode problem page url as input and extract the title
# read -p "Enter the LeetCode problem page URL: " leetcode_url
read -p "Enter the LeetCode problem name: " title

# Extracting the title from the URL
# title=$(curl -s "$leetcode_url" | grep -o '<title>[^<]*' | sed -e 's/<title>//' -e 's/ - LeetCode$//')

# Step 2: Create a Python file with the extracted title
file_name="LC-${title}.py"
touch "$file_name"

# Step 3: Use vim for multiline input
vim "$file_name"

# Step 4: Perform git commands
git add .
git commit -m "solve: $file_name"
git push

echo "Solution uploaded successfully!"
