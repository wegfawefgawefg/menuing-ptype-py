import pygame
import sys

from globals import FONT, HIGHLIGHT, WHITE
from mode import Mode
from vec2 import Vec2
from sounds import sound_effects

VIDEO_MENU_OPTIONS = ["Resolution", "Fullscreen", "Brightness", "Apply", "Back"]

"""
class State:
    def __init__(self) -> None:
        self.video_settings = VideoSettings()
        self.audio_settings = AudioSettings()
        self.controls_settings = ControlsSettings()

        self.resolution = Vec2(800, 600)
        self.last_mode = Mode.Main_Menu

        self.mode = Mode.Main_Menu

        self.menu_selection = 0


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
"""


def handle_events(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state.menu_selection -= 1
                if state.menu_selection < 0:
                    state.menu_selection = 0
                    sound_effects["cant"].stop()
                    sound_effects["cant"].play()
                else:
                    sound_effects["cursor_move"].stop()
                    sound_effects["cursor_move"].play()
            if event.key == pygame.K_DOWN:
                state.menu_selection += 1
                if state.menu_selection >= len(VIDEO_MENU_OPTIONS):
                    state.menu_selection = len(VIDEO_MENU_OPTIONS) - 1
                    sound_effects["cant"].stop()
                    sound_effects["cant"].play()
                else:
                    sound_effects["cursor_move"].stop()
                    sound_effects["cursor_move"].play()
            if event.key == pygame.K_RETURN:
                selection = VIDEO_MENU_OPTIONS[state.menu_selection]
                match selection:
                    case "Apply":
                        # if resolution changed, update it
                        something_changed = False
                        if state.video_settings.resolution != state.resolution:
                            state.resolution = Vec2(
                                state.video_settings.resolution[0],
                                state.video_settings.resolution[1],
                            )
                            something_changed = True
                        if state.video_settings.fullscreen:
                            pygame.display.set_mode(
                                state.resolution.as_tuple(), pygame.FULLSCREEN
                            )
                            something_changed = True
                        else:
                            pygame.display.set_mode(state.resolution.as_tuple())

                        if something_changed:
                            sound_effects["confirm"].stop()
                            sound_effects["confirm"].play()

                    case "Back":
                        state.mode = Mode.Settings_Menu
                        state.menu_selection = 0
                        sound_effects["cant"].stop()
                        sound_effects["cant"].play()
            # handle right left case
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                selection = VIDEO_MENU_OPTIONS[state.menu_selection]
                if selection == "Resolution":
                    # get index of current option
                    index = state.video_settings.resolution_options.index(
                        state.video_settings.resolution
                    )
                    # handle right left case
                    match event.key:
                        case pygame.K_RIGHT:
                            index += 1
                            if index >= len(state.video_settings.resolution_options):
                                index = 0
                            state.video_settings.resolution = (
                                state.video_settings.resolution_options[index]
                            )
                            sound_effects["right"].stop()
                            sound_effects["right"].play()
                        case pygame.K_LEFT:
                            index -= 1
                            if index < 0:
                                index = len(state.video_settings.resolution_options) - 1
                            state.video_settings.resolution = (
                                state.video_settings.resolution_options[index]
                            )
                            sound_effects["left"].stop()
                            sound_effects["left"].play()
                if selection == "Fullscreen":
                    # if enter, right, or left pressed
                    if (
                        event.key == pygame.K_RETURN
                        or event.key == pygame.K_RIGHT
                        or event.key == pygame.K_LEFT
                    ):
                        state.video_settings.fullscreen = (
                            not state.video_settings.fullscreen
                        )
                        if state.video_settings.fullscreen:
                            sound_effects["right"].stop()
                            sound_effects["right"].play()
                        else:
                            sound_effects["left"].stop()
                            sound_effects["left"].play()
                if selection == "Brightness":
                    # go up or down by 0.1
                    if event.key == pygame.K_RIGHT:
                        state.video_settings.brightness += 0.1
                        if state.video_settings.brightness > 1.0:
                            state.video_settings.brightness = 1.0
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            sound_effects["right"].stop()
                            sound_effects["right"].play()
                    if event.key == pygame.K_LEFT:
                        state.video_settings.brightness -= 0.1
                        if state.video_settings.brightness < 0.1:
                            state.video_settings.brightness = 0.1
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            sound_effects["left"].stop()
                            sound_effects["left"].play()


def draw(state, screen):
    screen.fill((0, 0, 0))

    five_percent = state.resolution.y // 20
    two_percent = state.resolution.y // 50
    ten_percent = state.resolution.y // 10

    cursor = ten_percent * 2
    center_x = state.resolution.x // 2

    # Draw the title.
    title = FONT.render("Main Menu", True, WHITE)
    title_rect = title.get_rect(center=(center_x, cursor))
    alpha = int(255 * state.video_settings.brightness)
    title.set_alpha(alpha)
    screen.blit(title, title_rect)

    cursor += ten_percent * 2

    # Draw the menu options.
    for i, option in enumerate(VIDEO_MENU_OPTIONS):
        match option:
            case "Resolution":
                option += f": {state.video_settings.resolution}"
            case "Fullscreen":
                option += f": {state.video_settings.fullscreen}"
            case "Brightness":
                # make sure brightness precision is only to 1 decimal place
                option += f": {state.video_settings.brightness * 100:.1f}%"

        color = HIGHLIGHT if i == state.menu_selection else WHITE
        text = FONT.render(option, True, color)
        text_rect = text.get_rect(center=(center_x, cursor))
        alpha = int(255 * state.video_settings.brightness)
        text.set_alpha(alpha)
        screen.blit(text, text_rect)
        cursor += five_percent

    pygame.display.flip()
