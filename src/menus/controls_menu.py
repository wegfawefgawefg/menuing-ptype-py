import pygame
import sys

from globals import FONT, HIGHLIGHT, WHITE
from mode import Mode

CONTROLS_MENU_OPTIONS = ["Jump", "Shoot", "Back"]


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
                if state.menu_selection >= len(CONTROLS_MENU_OPTIONS):
                    state.menu_selection = len(CONTROLS_MENU_OPTIONS) - 1
            if event.key == pygame.K_RETURN:
                selection = CONTROLS_MENU_OPTIONS[state.menu_selection]
                match selection:
                    case "Jump":
                        state.mode = Mode.Video_Menu
                        state.menu_selection = 0
                    case "Shoot":
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
    title = FONT.render("Main Menu", True, WHITE)
    title_rect = title.get_rect(center=(center_x, cursor))
    alpha = int(255 * state.video_settings.brightness)
    title.set_alpha(alpha)
    screen.blit(title, title_rect)

    cursor += ten_percent * 2

    # option += f": {state.audio_settings.music_volume * 100:.1f}%"
    # Draw the menu options.
    for i, option in enumerate(CONTROLS_MENU_OPTIONS):
        match option:
            case "Jump":
                option += f": {pygame.key.name(state.controls_settings.jump)}"
            case "Shoot":
                option += f": {pygame.key.name(state.controls_settings.shoot)}"

        color = HIGHLIGHT if i == state.menu_selection else WHITE
        text = FONT.render(option, True, color)
        text_rect = text.get_rect(center=(center_x, cursor))
        alpha = int(255 * state.video_settings.brightness)
        text.set_alpha(alpha)
        screen.blit(text, text_rect)
        cursor += five_percent

    pygame.display.flip()
