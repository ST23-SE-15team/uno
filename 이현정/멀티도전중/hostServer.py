# import socket

# def get_local_ipv4():
#     """
#     유저의 컴퓨터에서 IPv4 주소를 가져오는 함수
#     """
#     try:
#         hostname = socket.gethostname()
#         ip_address = socket.gethostbyname(hostname)
#         return ip_address
#     except socket.error as e:
#         print("IPv4 주소를 가져오는 중에 오류가 발생했습니다:", e)
#         return None

# # 서버 설정
# SERVER_IP = get_local_ipv4()
# SERVER_PORT = 5555

# if SERVER_IP:
#     print("로컬 IPv4 주소:", SERVER_IP)
# else:
#     print("로컬 IPv4 주소를 가져오지 못했습니다.")

# # 서버 소켓 시작
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((SERVER_IP, SERVER_PORT))
# server_socket.listen(1)

# # 클라이언트 접속 대기
# print("클라이언트 접속 대기 중...")
# client_socket, client_address = server_socket.accept()

# # 클라이언트와 통신 시작
# while True:
#     # 메시지 수신
#     data = client_socket.recv(1024)
#     if not data:
#         break

#     # 수신한 메시지 처리
#     received_message = data.decode()
#     print("받은 메시지:", received_message)

#     # 메시지 전송
#     message = "메시지를 받았습니다."
#     client_socket.send(message.encode())

#     # 통신 종료
#     client_socket.close()
#     server_socket.close()



