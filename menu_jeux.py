import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")

# Load background image
background_image = pygame.image.load("assets/arcade.jpg").convert()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 200, 0)

# Define fonts
title_font = pygame.font.SysFont(None, 48)
font = pygame.font.SysFont(None, 36)

# Function to display text on screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Function to create buttons
def draw_button(text, font, color, bg_color, surface, x, y, width, height):
    pygame.draw.rect(surface, bg_color, (x, y, width, height))
    pygame.draw.rect(surface, color, (x, y, width, height), 2)
    draw_text(text, font, color, surface, x + 10, y + 10)

# Function to get text input
def get_text_input(prompt):
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background_image, (0, 0))
        draw_text(prompt, font, WHITE, screen, 20, 20)
        draw_text(input_text, font, WHITE, screen, 20, 70)
        pygame.display.update()



# Main menu function
def main_menu():
    input_rect = pygame.Rect(300, 200, 200, 50)
    username = ""
    input_active = True
    cursor_visible = True
    cursor_timer = 0

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        screen.blit(background_image, (0, 0))

        # Toggle cursor visibility
        cursor_timer += 1
        if cursor_timer >= 5:  # Change blinking speed here
            cursor_visible = not cursor_visible
            cursor_timer = 0

        # Update input rectangle width based on username length
        text_surface = font.render(username, True, BLACK)
        input_rect.w = max(200, text_surface.get_width() + 10)

        pygame.draw.rect(screen, BLACK, input_rect, 2)
        text_surface = font.render("Enter Your Username:", True, BLACK)
        screen.blit(text_surface, (250, 150))
        text_surface = font.render(username, True, BLACK)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # Draw cursor if visible
        if cursor_visible:
            cursor_x = input_rect.x + text_surface.get_width() + 5
            cursor_y = input_rect.y + 5
            pygame.draw.line(screen, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + text_surface.get_height()), 2)

        pygame.display.flip()

    while True:
        screen.blit(background_image, (0, 0))
        draw_text(username, title_font, WHITE, screen, 20, 20)
        draw_text("Select a game:", font, WHITE, screen, 20, 100)

        # Display list of games
        game_selected = game_menu(username)

        # Display selected game and options
        game_options_menu(game_selected, username)

        pygame.display.update()


# Function to display game menu
def game_menu(username):
    # Here you can list your games
    games = ["Pong Beer", "Space Invader"]  # Adding "Space Invader" to the list
    game_selected = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_selected = (game_selected - 1) % len(games)
                elif event.key == pygame.K_DOWN:
                    game_selected = (game_selected + 1) % len(games)
                elif event.key == pygame.K_RETURN:
                    return games[game_selected]
                elif event.key == pygame.K_ESCAPE:
                    return None
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background_image, (0, 0))
        
        # Draw title
        draw_text("List of Games", title_font, WHITE, screen, 20, 20)
        
        # Display username in the top right
        draw_text(username, title_font, WHITE, screen, screen_width - 20 - title_font.size(username)[0], 20)

        for i, game in enumerate(games):
            if i == game_selected:
                draw_button(game, font, WHITE, LIGHT_GREEN, screen, 300, 200 + i * 50, 200, 40)
            else:
                draw_button(game, font, WHITE, GRAY, screen, 300, 200 + i * 50, 200, 40)
        pygame.display.update()

from menu_spaceinvader import main_invader


# Function to display game options menu
def game_options_menu(game_selected, username):
    options = ["Play", "About", "Back", "Exit"]
    option_selected = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    option_selected = (option_selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    option_selected = (option_selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[option_selected] == "Play":
                        if game_selected == "Space Invader":
                            main_invader()
                    elif options[option_selected] == "About":
                        print("About", game_selected)
                    elif options[option_selected] == "Back":
                        return
                    elif options[option_selected] == "Exit":
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background_image, (0, 0))
        
        # Display selected game in the top left
        draw_text(game_selected, title_font, WHITE, screen, 20, 20)
        
        # Display username in the top right
        draw_text(username, title_font, WHITE, screen, screen_width - 20 - title_font.size(username)[0], 20)

        for i, option in enumerate(options):
            if i == option_selected:
                draw_button(option, font, WHITE, LIGHT_GREEN, screen, 300, 200 + i * 50, 200, 40)
            else:
                draw_button(option, font, WHITE, GRAY, screen, 300, 200 + i * 50, 200, 40)
        pygame.display.update()


# Run the main menu function
main_menu()
