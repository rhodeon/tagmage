"""
    author: rhodeon
"""

import sys
import os
import eyed3

def set_working_dir():
    """
        Changes the working directory to source.
    """
    wrkdir = sys.argv[1]        # source path specified in command
    os.chdir(wrkdir)
    
def obtain_dest_dir():
    """
        Sets the destination directory to place files.
    """
    dest_dir = sys.argv[2]      # destination path specified in command
    return dest_dir


def list_files():
    """
        Creates a list of files in source directory
    """
    files = [f for f in os.listdir() if not f.startswith(".")]      # ignore hidden files
    return files

def main():
    """
        Creates folders and move files
    """
    dest_dir = obtain_dest_dir()    # destination directory
    raw_files = list_files()        # files in source directory

    for raw_name in raw_files:
        tagged_file = eyed3.load(raw_name)      # eyed3 object for tag info
        title_name = tagged_file.tag.title      # title tag
        artist_dir = tagged_file.tag.artist     # artist tag
        album_dir = tagged_file.tag.album       # album tag

        # skip file is either title, artist or album is missing
        if not title_name or not artist_dir or not album_dir:
            continue

        new_directory = os.path.join(dest_dir, artist_dir, album_dir)   # full path of directory to move file
        new_filename = os.path.join(new_directory, title_name) + ".mp3"     # new properly tagged name of file

        if not os.path.exists(new_directory):
            os.makedirs(new_directory)

        if not os.path.exists(new_filename):
            os.rename(raw_name, new_filename) 

if __name__ == "__main__":
    set_working_dir()
    obtain_dest_dir()
    main()
