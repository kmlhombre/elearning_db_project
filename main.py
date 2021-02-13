import wx

from loggingWindow import loggingFrame

if __name__ == "__main__":
    app = wx.App(False)
    frame = loggingFrame()
    app.MainLoop()