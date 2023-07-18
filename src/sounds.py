# sounds.py

import os
import pygame

pygame.mixer.init()


def load_sounds(directory):
    sounds = {}
    for filename in os.listdir(directory):
        if filename.endswith(".ogg"):
            key = os.path.splitext(filename)[0]
            sounds[key] = pygame.mixer.Sound(os.path.join(directory, filename))
    return sounds


def play_song(song_title):
    directory = "../assets/audio/music"
    file_name = f"{song_title}.ogg"
    pygame.mixer.music.load(os.path.join(directory, file_name))


sound_effects = load_sounds("../assets/audio/sound_effects/ui")
