import argparse
import pandas as pd
from crypto_utils import CryptoUtils
from network_utils import NetworkUtils

def handle_client(client_socket):
    try:
        # Recebe os dados do cliente
        encrypted_data = client_socket.recv(4096)
        decrypted_data = crypto.decrypt(encrypted_data)
        print(f"Received: {decrypted_data.decode()}")
        
        # Manipula os dados recebidos
        data = {'message': [decrypted_data.decode()]}
        df = pd.DataFrame(data)
        print(df)
    finally:
        client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ocean Trash Detection Encrypted Communication")
    parser.add_argument("mode", choices=["server", "client"], help="Run as server or client")
    parser.add_argument("--host", default="127.0.0.1", help="Host to connect or bind to")
    parser.add_argument("--port", type=int, default=65432, help="Port to connect or bind to")
    parser.add_argument("--key", required=True, help="Encryption key")
    parser.add_argument("--message", help="Message to send (for client mode)")

    args = parser.parse_args()

    crypto = CryptoUtils(key=args.key.encode())
    network = NetworkUtils(host=args.host, port=args.port)

    if args.mode == "server":
        network.start_server(handle_client)
    elif args.mode == "client":
        if not args.message:
            raise ValueError("Message is required in client mode")
        client_socket = network.connect_to_server()
        encrypted_message = crypto.encrypt(args.message.encode())
        network.send_data(client_socket, encrypted_message)
        client_socket.close()
