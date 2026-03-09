from pathlib import Path

import pygame

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
MUSIC_DIR = ASSETS_DIR / "audio" / "music"
SOUND_EFFECTS_DIR = ASSETS_DIR / "audio" / "sound_effects" / "ui"

sound_effects = {}


def load_sounds(directory):
    sounds = {}
    for sound_path in sorted(directory.glob("*.ogg")):
        sounds[sound_path.stem] = pygame.mixer.Sound(str(sound_path))
    return sounds


def init_audio():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    sound_effects.clear()
    sound_effects.update(load_sounds(SOUND_EFFECTS_DIR))


def play_song(song_title):
    pygame.mixer.music.load(str(MUSIC_DIR / f"{song_title}.ogg"))
