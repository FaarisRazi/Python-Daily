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
def remove(path, empty=False, inside=True, folders=False, types=['.txt', '.npy']):
    # -------------------------- File case:
    if isfile(path):
        os.remove(path)
        return True
    # -------------------------- Folder cases:
    # Remove files/folders inside directory
    if inside: 
        contained_files = files_in(path)

        if contained_files:
            
            for file in contained_files:
                file_path = path+file

                # Remove files with specfied extensions in directory
                if any(map(lambda ext: file.endswith(ext), types)):
                    os.remove(file_path)

                # Remove Folders in the directory if desired
                elif folders and not isfile(file):
                    shutil.rmtree(file_path)
                    
            return True

    # Else, Delete the whole directory itself.
    confirm = input('Removing your whole directory ... Confirm with "y"/"Y", or Cancel with any key: ')

    if 'y' == confirm.strip().lower():
        shutil.rmtree(path)
        print('File Removed.')
        return True
    
    print('Directory-Deletion Cancelled!')
