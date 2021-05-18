"""
    author: rhodeon
"""

import sys

from operations.sort_files import *
from operations.embed_lyrics import *

flags = ["--sort", "--embed"]   # list of valid argument flags

def main():
    args = sys.argv
    flag = args[1]
    
    if flag not in flags:
        print(f"{flag} is not a valid flag.  See: {flags}")
        return

    src_dir = args[2]
    set_working_dir(src_dir)
    songs = list_files()    # files in source directory

    if flag == flags[0]:
        dest_dir = args[3]
        sort_files(songs, dest_dir)
    
    elif flag == flags[1]:
        embed_lyrics(songs)
    
if __name__ == "__main__":
    main()
