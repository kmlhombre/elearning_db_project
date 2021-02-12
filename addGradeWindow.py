import wx

from errorWindow import errorFrame
from successWindow import successFrame


class addGradeFrame(wx.Frame):

    def __init__(self, students):
        super().__init__(parent=None, title="Add Grade")
        self.SetSize(400, 300)
        self.SetBackgroundColour('pink')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(panel, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer(1)

        self.SetSizer(sizer)

        self.choice = wx.Choice(panel, choices=students)
        self.text_ctrl3 = wx.TextCtrl(panel)

        my_btn = wx.Button(panel, label='Confirm', pos=(20, 20), size=(300, 50))

        # akcje obiektow
        self.choice.SetSelection(0)
        self.text_ctrl3.AppendText("Grade")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        # rozmieszczenie obiektow w oknie
        my_sizer.Add(self.choice, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(self.text_ctrl3, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):

        # TODO update z Jędrzejem
        grade = self.text_ctrl3.GetValue()

        # TODO add grades to the database. Call proper function.
        # TODO get response message?
        isGradeAdded = False
        # Mock - to replacec
        b = event.GetEventObject()
        print(b.GetLabel(), "Add grade success")
        self.Hide()

        if isGradeAdded:
            successFrame('Successfully added a grade!')
        else:
            errorFrame('Some error has occured')


