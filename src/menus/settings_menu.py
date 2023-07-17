import pygame
import sys

from globals import FONT, HIGHLIGHT, WHITE
from mode import Mode
from . import (
    audio_menu,
    controls_menu,
    main_menu,
    video_menu,
)


SETTINGS_MENU_OPTIONS = ["Video", "Audio", "Controls", "Back"]


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
                if state.menu_selection >= len(SETTINGS_MENU_OPTIONS):
                    state.menu_selection = len(SETTINGS_MENU_OPTIONS) - 1
            if event.key == pygame.K_RETURN:
                selection = SETTINGS_MENU_OPTIONS[state.menu_selection]
                match selection:
                    case "Video":
                        state.mode = Mode.Video_Menu
                        state.menu_selection = 0
                    case "Audio":
                        state.mode = Mode.Audio_Menu
                        state.menu_selection = 0
                    case "Controls":
                        state.mode = Mode.Controls_Menu
                        state.menu_selection = 0
                    case "Back":
                        state.mode = Mode.Main_Menu
                        state.menu_selection = 0


def draw(state, screen):
    screen.fill((0, 0, 0))

    five_percent = state.resolution.y // 20
    two_percent = state.resolution.y // 50
    ten_percent = state.resolution.y // 10

    cursor = ten_percent * 2
    center_x = state.resolution.x // 2

    # Draw the title.
    title = FONT.render("Settings", True, WHITE)
    title_rect = title.get_rect(center=(center_x, cursor))
    screen.blit(title, title_rect)

    cursor += ten_percent * 2

    # Draw the menu options.
    for i, option in enumerate(SETTINGS_MENU_OPTIONS):
        color = HIGHLIGHT if i == state.menu_selection else WHITE
        text = FONT.render(option, True, color)
        text_rect = text.get_rect(center=(center_x, cursor))
        screen.blit(text, text_rect)
        cursor += five_percent

    pygame.display.flip()
