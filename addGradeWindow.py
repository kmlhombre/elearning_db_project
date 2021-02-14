import wx

import teacherWindow
from errorWindow import errorFrame
from successWindow import successFrame

from methods import add_grade


class addGradeFrame(wx.Frame):

    def __init__(self, students, subject):
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

        self.students = students
        self.subject = subject
        new_choices = []
        for s in self.students:
            new_choices.append(s[1] + ' ' + s[2])

        self.choice = wx.Choice(panel, choices=new_choices)
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
        grade = self.text_ctrl3.GetValue()
        student = self.choice.GetCurrentSelection()
        student_tmp = self.students[student]

        isGradeAdded = False
        # TODO add grades to the database. Call proper function.
        # TODO get response message?

        isGradeAdded = add_grade(student_tmp[0], self.subject, grade)


        # Mock - to replacec
        b = event.GetEventObject()
        print(b.GetLabel(), "Add grade success")
        self.Close()

        if isGradeAdded:
            successFrame('Successfully added a grade!')
        else:
            errorFrame('Some error has occured')


