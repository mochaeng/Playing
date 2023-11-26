from threading import Thread
import socket
import json


def handle_conn(conn: socket.socket, addr):
    print(f'Server has connected with client: {addr}')

    while True:
        raw_data = conn.recv(1024)
        print(raw_data)

        json_data = json.loads(raw_data)
        print(f"Client [{addr}] sent: {json_data['msg']}")

        conn.sendall(b'ack')


def start_server():
    server_address = ('10.0.0.1', 50052)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(server_address)
        s.listen()

        while True:
            conn, addr = s.accept()
            Thread(target=handle_conn, args=[conn, addr]).start()


if __name__ == "__main__":
    start_server()
