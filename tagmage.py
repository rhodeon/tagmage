"""
    author: rhodeon
"""

import sys

from sort_files import *

flags = ["--sort", "--merge"]   # list of valid argument flags

def main():
    args = sys.argv
    flag = args[1]
    
    if flag not in flags:
        print("Enter a valid flag")
        return

    src_dir = args[2]
    set_working_dir(src_dir)
    raw_files = list_files()    # files in source directory

    if flag == "--sort":
        dest_dir = args[3]
        sort_files(raw_files, dest_dir)
    
if __name__ == "__main__":
    main()
