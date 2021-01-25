import socket

HOST = 'localhost'
PORT = 8002
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            conn.sendall(data)
