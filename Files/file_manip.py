# Handy functions for file/folder manipulation to be added InshaAllah! 
import os

# Get the  current working-directory
current_dir = os.getcwd().replace('\\','/')+'/'

# Check if input path is for a file. (else it is a folder)
isfile = lambda path: os.path.isfile(path)

# Check if file is of a given extension/type 
istype = lambda file, ext='': file.endswith(ext)

# Get list of files/folders in directory
files_in = lambda path: os.listdir(path)

# Remove files with specific types and/or folders in a directory
def remove(path, empty=False, folders=False, types=[]):
    if empty:
        return os.rmdir(path)
    
    # If path given is a Folder/Directory
    if not isfile(path):

        # Delete all files
        for file in files_in(path):

            # Remove files with specfied extensions
            if any(map(lambda ext: file.endswith(ext), types)):
                os.remove(path+file)

            # Remove Folders in the directory if desired
            # elif folders and not isfile(file):

        return True
