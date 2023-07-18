import pygame
import sys

from globals import FONT, HIGHLIGHT, WHITE
from mode import Mode
from sounds import sound_effects

AUDIO_MENU_OPTIONS = ["Music", "Sound Effects", "Back"]


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
            if event.key == pygame.K_DOWN:
                state.menu_selection += 1
                if state.menu_selection >= len(AUDIO_MENU_OPTIONS):
                    state.menu_selection = len(AUDIO_MENU_OPTIONS) - 1
            if event.key == pygame.K_RETURN:
                selection = AUDIO_MENU_OPTIONS[state.menu_selection]
                match selection:
                    case "Back":
                        state.mode = Mode.Settings_Menu
                        state.menu_selection = 0
                        sound_effects["cant"].stop()
                        sound_effects["cant"].play()
            # handle right left case
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                selection = AUDIO_MENU_OPTIONS[state.menu_selection]
                if selection == "Music":
                    # go up or down by 0.1
                    if event.key == pygame.K_RIGHT:
                        state.audio_settings.music_volume += 0.1
                        if state.audio_settings.music_volume > 1.0:
                            state.audio_settings.music_volume = 1.0
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            pygame.mixer.music.set_volume(
                                state.audio_settings.music_volume
                            )
                            sound_effects["right"].stop()
                            sound_effects["right"].play()
                    if event.key == pygame.K_LEFT:
                        state.audio_settings.music_volume -= 0.1
                        if state.audio_settings.music_volume < 0.0:
                            state.audio_settings.music_volume = 0.0
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            pygame.mixer.music.set_volume(
                                state.audio_settings.music_volume
                            )
                            sound_effects["left"].stop()
                            sound_effects["left"].play()
                if selection == "Sound Effects":
                    # go up or down by 0.1
                    if event.key == pygame.K_RIGHT:
                        state.audio_settings.sfx_volume += 0.1
                        if state.audio_settings.sfx_volume > 1.0:
                            state.audio_settings.sfx_volume = 1.0
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            for name, sound_effect in sound_effects.items():
                                sound_effect.set_volume(state.audio_settings.sfx_volume)
                            sound_effects["right"].stop()
                            sound_effects["right"].play()
                    if event.key == pygame.K_LEFT:
                        state.audio_settings.sfx_volume -= 0.1
                        if state.audio_settings.sfx_volume < 0.0:
                            state.audio_settings.sfx_volume = 0.0
                            sound_effects["cant"].stop()
                            sound_effects["cant"].play()
                        else:
                            for name, sound_effect in sound_effects.items():
                                sound_effect.set_volume(state.audio_settings.sfx_volume)
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
    for i, option in enumerate(AUDIO_MENU_OPTIONS):
        match option:
            case "Music":
                option += f": {state.audio_settings.music_volume * 100:.1f}%"
            case "Sound Effects":
                option += f": {state.audio_settings.sfx_volume * 100:.1f}%"

        color = HIGHLIGHT if i == state.menu_selection else WHITE
        text = FONT.render(option, True, color)
        text_rect = text.get_rect(center=(center_x, cursor))
        alpha = int(255 * state.video_settings.brightness)
        text.set_alpha(alpha)
        screen.blit(text, text_rect)
        cursor += five_percent

    pygame.display.flip()
