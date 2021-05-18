import os
import eyed3

from utils import *

def embed_lyrics(songs):
    """
        Embeds synchronized lyrics files in songs with corresponding names
    """

    for song in songs:
        lyrics = os.path.splitext(song)[0] + ".lrc"

        if os.path.exists(lyrics):  # corresponding lyrics file exists
            with open(lyrics) as lrc:
                lyrics_string = lrc.read()
            
            tagged_song = eyed3.load(song)
            tagged_song.tag.lyrics.set(text = lyrics_string)
            tagged_song.tag.save()
            print(song)     # Displays the songs affected to the user
