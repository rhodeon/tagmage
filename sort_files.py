import os
import eyed3

from utils import *

def sort_files(songs, dest):
    """
        Creates folders and move files
    """
    dest_dir = obtain_dest_dir(dest)    # destination directory

    for song in songs:
        tagged_file = eyed3.load(song)      # eyed3 object for tag info
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
            os.rename(song, new_filename) 