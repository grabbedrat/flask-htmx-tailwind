import socket
import threading
import redis

# Connect to Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def handle_client_connection(client_socket):
    try:
        while True:
            # Receive audio data from client
            audio_data = client_socket.recv(1024)
            if not audio_data:
                break

            # Here, you would process the audio data
            # For simplicity, let's just send raw data to Redis
            redis_client.publish('audio_channel', audio_data)

    finally:
        client_socket.close()

def start_tcp_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)  # Listen for up to 5 connections

    print(f"Server listening on port {port}")

    while True:
        client_sock, address = server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client_connection, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    start_tcp_server(9999)
