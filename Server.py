import socket
import threading
from colorama import Fore, Style
from modules.getServerIp import getServerip

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = (getServerip(), 8888)
s.bind(addr)

s.listen(1)
print(
    f"{Fore.BLUE} Server is listening at {addr[0]}:{addr[1]}{Style.RESET_ALL}")


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
