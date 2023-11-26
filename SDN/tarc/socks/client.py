import socket
import json


def start_client():
    server_address = ('10.0.0.1', 50052)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(server_address)

        while True:
            print('Type > ', end="")
            msg = input()

            data = {'msg': msg}
            json_data = json.dumps(data).encode()
            s.sendall(json_data)

            msg_from_server = s.recv(1024)
            print(msg_from_server)


if __name__ == "__main__":
    start_client()
