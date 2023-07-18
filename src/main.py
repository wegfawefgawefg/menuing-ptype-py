import pygame
import sys
from globals import FONT, WHITE
from menus import audio_menu, controls_menu, settings_menu, video_menu
from vec2 import Vec2
from sounds import play_song


from mode import Mode
from menus import (
    main_menu,
)


class State:
    def __init__(self) -> None:
        self.video_settings = VideoSettings()
        self.audio_settings = AudioSettings()
        self.controls_settings = ControlsSettings()

        self.resolution = Vec2(800, 600)
        self.last_mode = Mode.Main_Menu

        self.mode = Mode.Main_Menu

        self.menu_selection = 0
        self.choosing_control_binding = False


class VideoSettings:
    def __init__(self) -> None:
        self.resolution = (800, 600)
        self.fullscreen = False
        self.brightness = 1.0
        self.vsync = True

        self.resolution_options = [
            (800, 600),
            (1024, 768),
            (1280, 720),
            (1280, 1024),
            (1920, 1080),
        ]


class AudioSettings:
    def __init__(self) -> None:
        self.music_volume = 1.0
        self.sfx_volume = 1.0


class ControlsSettings:
    def __init__(self) -> None:
        self.jump = pygame.K_SPACE
        self.shoot = pygame.MOUSEBUTTONDOWN


def handle_events(state):
    match state.mode:
        case Mode.Main_Menu:
            main_menu.handle_events(state)
        case Mode.Settings_Menu:
            settings_menu.handle_events(state)
        case Mode.Playing:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        state.mode = Mode.Main_Menu
        case Mode.Video_Menu:
            video_menu.handle_events(state)
        case Mode.Audio_Menu:
            audio_menu.handle_events(state)
        case Mode.Controls_Menu:
            controls_menu.handle_events(state)


def step(state):
    """engine specific"""
    match state.mode:
        case Mode.Main_Menu:
            pass
        case Mode.Playing:
            pass
        case Mode.Video_Menu:
            pass
        case Mode.Audio_Menu:
            pass
        case Mode.Controls_Menu:
            pass


def draw(state, screen):
    match state.mode:
        case Mode.Main_Menu:
            main_menu.draw(state, screen)
        case Mode.Settings_Menu:
            settings_menu.draw(state, screen)
        case Mode.Playing:
            # just put the word playing in the middle of the screen

            text = FONT.render("Playing", True, WHITE)
            text_rect = text.get_rect(
                center=(state.resolution.x // 2, state.resolution.y // 4)
            )
            screen.blit(text, text_rect)
            text = FONT.render("(press q to go back)", True, WHITE)
            text_rect = text.get_rect(
                center=(state.resolution.x // 2, state.resolution.y // 2)
            )
            screen.blit(text, text_rect)
        case Mode.Video_Menu:
            video_menu.draw(state, screen)
        case Mode.Audio_Menu:
            audio_menu.draw(state, screen)
        case Mode.Controls_Menu:
            controls_menu.draw(state, screen)


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    state = State()
    screen = pygame.display.set_mode(state.resolution.as_tuple())

    play_song("menu")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)  # loop

    clock = pygame.time.Clock()
    while True:
        handle_events(state)
        step(state)
        screen.fill((0, 0, 0))
        draw(state, screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
