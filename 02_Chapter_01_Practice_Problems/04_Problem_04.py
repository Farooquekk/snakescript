#  Write a Program to print the contents of the directory using OS module in Python Using AI tool.

import os

# Specify the directory path
directory_path = '/22SW040/OSClab2'

# List all paths and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)