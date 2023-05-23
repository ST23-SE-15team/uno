import pygame
import pygame_gui

def run():

    pygame.init()
    clock = pygame.time.Clock()

    # 화면 크기 설정
    window_width, window_height = 800, 600
    window_surface = pygame.display.set_mode((window_width, window_height))

    # 팝업 관리자 생성
    manager = pygame_gui.UIManager((window_width, window_height))

    # IP 입력 창 생성
    input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 200), (200, 30)),
                                                    manager=manager)

    # 버튼 생성
    join_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (100, 30)),
                                            text='Join',
                                            manager=manager)
    # # 버튼 배경색 및 텍스트 색상 변경
    # input_box.bg_color = pygame.Color('#ffffff')  # 배경색
    # #input_box.text_color = pygame.Color('#FFFFFF')  # 텍스트 색상
    # join_button.bg_color = pygame.Color('#FF0000')  # 배경색



    # 이벤트 루프
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == join_button:
                        ip_address = input_box.text
                        #join_room(ip_address)  # join_room 함수 호출 또는 다른 동작 수행
                        
            manager.process_events(event)

        manager.update(time_delta)
        
        window_surface.fill((255, 255, 255))
        manager.draw_ui(window_surface)

        pygame.display.update()

    pygame.quit()
