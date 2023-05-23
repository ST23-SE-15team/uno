import pygame
pygame.init()
import settings
import singlegame
import modeChoosepage
import json
import achievpage



def load_custom_keys():
    global custom_keys
    with open('keySetting.json', 'r') as f:
        custom_keys = json.load(f)
        
#sound_settings.json 파일에 있는 볼륨 크기를 불러와서 적용합니다.
pygame.mixer.music.load('./이채은/sound/배경1.mp3')
with open('sound_settings.json', 'r') as file:
    sound_settings = json.load(file)
volume_all = sound_settings['volume_all']
pygame.mixer.music.set_volume(volume_all / 100)
pygame.mixer.music.play(-1)


# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("UNO")
keybord = pygame.image.load("./이현정/키보드2.png")
keybord = pygame.transform.scale(keybord, (150, 130))
mouse = pygame.image.load("./이현정/마우스2.png")
mouse = pygame.transform.scale(mouse,(150,150))
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
# Define fonts
title_font = pygame.font.SysFont('comicsansms', 80)
menu_font = pygame.font.SysFont('comicsansms', 50)
popup_menu_font = pygame.font.SysFont('comicsansms', 50)
# Create text surfaces
title_text = title_font.render('UNO', True, BLACK)
# Set up menu buttons
button_width = 200
button_height = 100
button_padding = 20
# Define menu items
menu_items = [
    {"text": "Game Mode", "pos": (WIN_WIDTH//2, 200)},
    {"text": "Achievement", "pos": (WIN_WIDTH//2, 300)},
    {"text": "Settings", "pos": (WIN_WIDTH//2, 400)},
    {"text": "Exit", "pos": (WIN_WIDTH//2, 500)}
]
# Set up the cursor
cursor_img = pygame.Surface((20, 20))
cursor_img.set_colorkey((0, 0, 0))
# cursor_img.fill(WHITE)
cursor_rect = cursor_img.get_rect()
# Set up the menu
selected_item = 0
# Main game loop
running = True
while running:
    # Handle events
    load_custom_keys()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == custom_keys['up']:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == custom_keys['down']:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == custom_keys['return']:
                if selected_item == 0:
                    modeChoosepage.modeChoose()
                elif selected_item == 1:
                    achievpage.achiev()  
                elif selected_item == 2:
                    settings.settings_screen()
                elif selected_item == 3:
                    running = False
        elif event.type == pygame.MOUSEMOTION:
            cursor_rect.center = event.pos
        # Handle mouse button down events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("click!")
            if event.button == 1:
                for i, item in enumerate(menu_items):
                    button_rect = pygame.Rect(item["pos"][0] - button_width/2, item["pos"][1] - button_height/2, button_width, 70)
                    if button_rect.collidepoint(event.pos):
                        selected_item = i
                        if selected_item == 0:
                            modeChoosepage.modeChoose()
                        elif selected_item == 1:
                            achievpage.achiev()  
                        elif selected_item == 2:
                            settings.settings_screen()
                        elif selected_item == 3:
                            running = False
    # Draw the menu
    win.fill(WHITE)
    #pygame.draw.rect(win, GRAY, (WIN_WIDTH//2 - 150, 150, 300, 300))
    win.blit(title_text,((WIN_WIDTH - title_text.get_width()) / 2, 50))
    win.blit(keybord,(50,25))
    win.blit(mouse,(600,20))
    for i, item in enumerate(menu_items):
        text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
        rect = text.get_rect(center=item["pos"])
        if rect.collidepoint(cursor_rect.center):
            #text=GRAY
            text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
        win.blit(text, rect)
    # Draw the cursor
    win.blit(cursor_img, cursor_rect)
    # Update the display
    pygame.display.update()
pygame.quit()
