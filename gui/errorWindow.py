import wx


class errorFrame(wx.Frame):

    def __init__(self, message):
        super().__init__(parent=None, title="Error")
        self.message = message
        self.SetSize(200, 100)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('orange')
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        #elementy zawarte w oknie
        txt = wx.StaticText(panel, -1, message, (100, 50), (160, -1), wx.ALIGN_CENTER)
        txt.SetForegroundColour('white')
        my_btn = wx.Button(panel, label='Try Again')

        #akcja dla przycisku
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        #rozmieszczenie obiektow w oknie
        my_sizer.Add(txt, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        self.Hide()