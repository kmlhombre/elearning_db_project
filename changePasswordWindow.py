import wx

from successWindow import successFrame
from methods import change_password


class changePasswordFrame(wx.Frame):

    def __init__(self, logged_user):
        super().__init__(parent=None, title="elearning")
        self.SetSize(400, 300)
        self.SetBackgroundColour('pink')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.logged_user_id = logged_user

        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(panel, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer(1)

        self.SetSizer(sizer)

        #elementy zawarte w oknie
        self.txt = wx.TextCtrl(panel)
        my_btn = wx.Button(panel, label='Change Password')
        #akcje obiektow
        self.txt.AppendText("New Password")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        #rozmieszczenie obiektow w oknie
        my_sizer.Add(self.txt, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        #TODO wpisac nowe haslo do bazy:
        newPassword = self.txt.GetValue()

        change_password(self.logged_user_id, newPassword)

        successFrame('Password has been changed')
        self.Hide()
