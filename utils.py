import os

"""
    Set of common functions
"""

def set_working_dir(src):
    """
        Changes the working directory to source.
    """
    wrkdir = src        # source path specified in command
    os.chdir(wrkdir)

def obtain_dest_dir(dest):
    """
        Sets the destination directory to place files.
    """
    dest_dir = dest      # destination path specified in command
    return dest_dir
    
def list_files():
    """
        Creates a list of files in source directory
    """
    files = [f for f in os.listdir() if f.endswith(".mp3")]      # select only mp3 files
    return files