#List of Dictionaries on files in a working directory

#!/usr/bin/env python3.7


# Get built-in Module 

from pathlib import Path

# Specify the directory where we will be listing its files

Directory_current = Path.cwd()




#Empty list to store file info

Files = []



# iterates all objects in the current direcotry incluidng its file attributes & information
if not Directory_current:

    Directory_current = Path.cwd()

    Files = []


for file in list(Directory_current.iterdir()):
    
    file_path = file 
    name = Path(file_path).stem 
    size = Path(file_path).stat().st_size

    
    Files.append({'name': name, 'size': size})
    print(*Files,sep="\n")
   

