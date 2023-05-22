import pygame
pygame.init()
import singlegame
import storymode1
import json
import lobby
import multiRoom2

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

def load_custom_keys():
    global custom_keys
    with open('keySetting.json', 'r') as f:
        custom_keys = json.load(f)

def modeChoose():
    # 게임화면의 크기 설정
    # WIDTH = 800
    # HEIGHT = 600

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)

    background_color = (255, 255, 255)  # 흰색

    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # Draw the menu
    win.fill(WHITE)

    pygame.display.set_caption("UNO")
    keybord = pygame.image.load("./이현정/키보드2.png")
    keybord = pygame.transform.scale(keybord, (150, 130))
    mouse = pygame.image.load("./이현정/마우스2.png")
    mouse = pygame.transform.scale(mouse,(150,150))

    # Define fonts
    title_font = pygame.font.SysFont('comicsansms', 80)
    mode_menu_font = pygame.font.SysFont('comicsansms', 50)

    # Set up menu buttons
    button_width = 200
    button_height = 100
    button_padding = 20
    
    # Create text surfaces
    title_text = title_font.render('UNO', True, BLACK)

    # Define menu items
    mode_items = [
    {"text": "Only Play", "pos": (WIN_WIDTH//2, 200)},
    {"text": "Story Mode", "pos": (WIN_WIDTH//2, 310)},
    {"text": "Multi Play", "pos": (WIN_WIDTH//2, 420)},
    {"text": "Back", "pos": (WIN_WIDTH//2, 530)}
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
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == custom_keys['up']:
                    selected_item = (selected_item - 1) % len(mode_items)
                elif event.key == custom_keys['down']:
                    selected_item = (selected_item + 1) % len(mode_items)
                elif event.key == custom_keys['return']:
                    if selected_item == 0:
                        lobby.lobby()
                    elif selected_item == 1:
                        storymode1.story_map1()
                    elif selected_item == 2:
                        multiRoom2.run()
                    elif selected_item == 3:
                        running = False

            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
            # Handle mouse button down events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click!")
                if event.button == 1:
                    for i, item in enumerate(mode_items):
                        button_rect = pygame.Rect(item["pos"][0] - button_width/2, item["pos"][1] - button_height/2, button_width, button_height)
                        if button_rect.collidepoint(event.pos):
                            selected_item = i
                            if selected_item == 0:
                                lobby.lobby()
                            elif selected_item == 1:
                                storymode1.story_map1()
                            elif selected_item == 2:
                                multiRoom2.run()
                            elif selected_item == 3:
                                running = False


        # Draw the menu
        win.fill(WHITE)
        #pygame.draw.rect(win, GRAY, (WIN_WIDTH//2 - 150, 150, 300, 300))
        win.blit(title_text,((WIN_WIDTH - title_text.get_width()) / 2, 50))
        win.blit(keybord,(50,25))
        win.blit(mouse,(600,20))
        for i, item in enumerate(mode_items):
            text = mode_menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
            rect = text.get_rect(center=item["pos"])
            if rect.collidepoint(cursor_rect.center):
                #text=GRAY
                text = mode_menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
            win.blit(text, rect)

        # Draw the cursor
        win.blit(cursor_img, cursor_rect)

        # Update the display
        pygame.display.update()

#pygame.quit()
