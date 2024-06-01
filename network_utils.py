import socket

class NetworkUtils:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def start_server(self, handle_client):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            handle_client(client_socket)

    def connect_to_server(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        return client_socket

    def send_data(self, sock: socket.socket, data: bytes):
        sock.sendall(data)

    def receive_data(self, sock: socket.socket, buffer_size: int = 4096) -> bytes:
        return sock.recv(buffer_size)
