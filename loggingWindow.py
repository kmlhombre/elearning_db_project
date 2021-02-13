import wx

from errorWindow import errorFrame
from parentWindow import parentFrame
from studentWindow import studentFrame
from teacherWindow import teacherFrame

from methods import login_user


class loggingFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(400, 300)
        self.SetBackgroundColour('pink')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        #TEST GITHUBA LOLOLOL
        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(panel, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer(1)

        self.SetSizer(sizer)

        # elementy zawarte w oknie
        self.text_ctrl1 = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)

        my_btn = wx.Button(panel, label='Log in', pos=(20, 20), size=(300, 50))

        # akcje obiektow
        self.text_ctrl1.AppendText("Login")
        self.text_ctrl2.AppendText("Password")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        # rozmieszczenie obiektow w oknie
        my_sizer.Add(self.text_ctrl1, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):

        # TODO zrobic funkcje ktora loguje uzytkownika
        login = self.text_ctrl1.GetValue()
        password = self.text_ctrl2.GetValue()
        print(password)
        # tutaj potrzebna funkcja logujaca
        user, logged_status = login_user(login, password)

        if user is not None and user.login == login:
            is_logged = True
        # na potrzebny testowania
        # logged_user_id = 1
        # logged_status = "Student"
        # is_logged = True

        if logged_status == "Student" and is_logged:
            studentFrame(login)
            self.Close()
        elif logged_status == "Parent" and is_logged:
            parentFrame(login)
            self.Close()
        elif logged_status == "Teacher" and is_logged:
            teacherFrame(login)
            self.Close()
        else:
            errorFrame('Wrong login data')
