# multiRoom2.py
import pygame
from pygame.locals import *
import socket
import threading

# 서버 설정
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

# Pygame 초기화
pygame.init()

# 창 크기 설정
window_width, window_height = 800, 600
window_surface = pygame.display.set_mode((window_width, window_height))

# 선택 변수
selected_option = None

# 방 창 생성 함수
def create_room():
    # 방 생성 로직 작성
    # 서버 설정, IP 주소 등
    
    # 예시로 방 번호 출력
    print("방이 생성되었습니다.")

    # 서버 소켓 시작
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)

    # 클라이언트 접속 대기
    print("클라이언트 접속 대기 중...")
    client_socket, client_address = server_socket.accept()

    # 클라이언트와 통신 시작
    while True:
        # 메시지 수신
        data = client_socket.recv(1024)
        if not data:
            break

        # 수신한 메시지 처리
        received_message = data.decode()
        print("받은 메시지:", received_message)

        # 메시지 전송
        message = "메시지를 받았습니다."
        client_socket.send(message.encode())

    # 통신 종료
    client_socket.close()
    server_socket.close()

# 유저 창 생성 함수
def join_room(ip_address):
    # 유저 참가 로직 작성
    # 클라이언트 설정, IP 주소 등
    
    # 예시로 IP 주소 출력
    print("방에 참가하였습니다. IP 주소:", ip_address)

    # 서버에 접속
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, SERVER_PORT))

    # 통신 시작
    while True:
        # 메시지 입력
        message = input("메시지를 입력하세요: ")

        # 메시지 전송
        client_socket.send(message.encode())

        # 서버로부터 응답 받기
        data = client_socket.recv(1024)
        received_message = data.decode()
        print("받은 응답:", received_message)

        # 종료 조건
        if message == "exit":
            break

    # 통신 종료
    client_socket.close()

# 버튼 클래스
class Button:
    def __init__(self, text, rect):
        self.rect = pygame.Rect(rect)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# 버튼 생성
host_button = Button("HOST", (100, 200, 200, 50))
user_button = Button("USER", (100, 300, 200, 50))

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if host_button.is_clicked(pos):
                selected_option = "host"
            elif user_button.is_clicked(pos):
                selected_option = "user"

    # 배경 그리기
    window_surface.fill((255, 255, 255))

    # 버튼 그리기
    host_button.draw(window_surface)
    user_button.draw(window_surface)

    # 선택된 옵션에 따라 동작 수행
    if selected_option == "host":
        create_room()
        running = False
    elif selected_option == "user":
        # IP 주소 입력 받기
        ip_address = input("방장의 IP 주소를 입력하세요: ")
        join_room(ip_address)
        running = False

    pygame.display.update()

# Pygame 종료
pygame.quit()
