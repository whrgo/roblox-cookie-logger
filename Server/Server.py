import socket
import threading
from colorama import Fore, Style


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.75.43', 8888))

s.listen(1)


def handle_tcp(sock, addr):
    print(f"{Fore.GREEN}New Connection From {Fore.LIGHTBLUE_EX} %s:%s {Style.RESET_ALL}" % addr)

    while True:
        data = sock.recv(1024).decode()
        if not data:
            break
        print(data)

    sock.close()


if __name__ == '__main__':
    sock, addr = s.accept()
    threading.Thread(target=handle_tcp, args=(sock, addr)).start()

while True:
    pass
