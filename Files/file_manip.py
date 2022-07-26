# Handy functions for file/folder manipulation to be added InshaAllah! 
import os

# Get the  current working-directory
current_dir = os.getcwd().replace('\\','/')+'/'

# Get list of files/folders in directory
files_in = lambda path: os.listdir(path)

def remove(path, empty=False):
  if empty:
    return os.rmdir(path)
