import os
import eyed3

from utils import *

successes = []
failures = []

def embed_lyrics(songs):
    """
        Embeds synchronized lyrics files in songs with corresponding names
    """

    for song in songs:
        lyrics = os.path.splitext(song)[0] + ".lrc"

        if os.path.exists(lyrics):  # corresponding lyrics file exists
            try:
                with open(lyrics) as lrc:
                    lyrics_string = lrc.read()
                
                tagged_song = eyed3.load(song)
                tagged_song.tag.lyrics.set(text = lyrics_string)    # embed lyrics
                os.remove(lyrics)   # delete lyrics file
                
                tagged_song.tag.save()
                successes.append(song)

            except:
                failures.append(song)
                continue

    displayResult()

def displayResult():
    if successes:
        print("SUCCESSFUL:")
        for song in successes:
            print(song)
        print()

    if failures:
        print("FAILED:")
        for song in failures:
            print(song)
        print()
