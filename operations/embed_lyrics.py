import os
import eyed3

from utils import *

successes = []
failures = {}

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
                
                # embed lyrics
                try:    # check if lyric already exists and replace
                    tagged_song.tag.lyrics[0].text = lyrics_string
                except IndexError:  # lyric doesn't exist. create new one
                    tagged_song.tag.lyrics.set(text = lyrics_string, lang="")
                
                os.remove(lyrics)   # delete lyrics file
                tagged_song.tag.save()
                successes.append(song)

            except Exception as reason:
                failures[song] = reason
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
        for song, reason in failures.items():
            print(f"{song} - {reason}")
        print()
