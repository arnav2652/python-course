import os

# Select the directory whose content you want to list
directory_path = '/'

# use the os module to list the directory path
contents = os.listdir(directory_path)


# print the contents of the directory
print(contents)
