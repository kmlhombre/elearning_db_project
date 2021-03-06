import wx

from changePasswordWindow import changePasswordFrame

from methods import display_grades, get_subjects

class studentPanel(wx.Panel):
    def __init__(self, parent, logged_user):
        super().__init__(parent)
        main_sizer = wx.GridBagSizer(10, 10)
        self.row_obj_dict = {}
        self.current_folder_path = None

        self.logged_user_id = logged_user

        # stworzenie tabeli
        self.list_ctrl = wx.ListCtrl(self, size=(800, 600), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, "Subject", width=140)
        self.list_ctrl.SetColumnWidth(0, 120)
        self.list_ctrl.SetScrollbar(wx.HORIZONTAL, 0, 16, 50)
        for index in range(1, 20):
            self.list_ctrl.InsertColumn(index, "Grade", width=60)
            self.list_ctrl.SetColumnWidth(index, 60)

        self.subjects = []

        # przedmioty
        sub_tmp = get_subjects()
        for subject in sub_tmp:
            self.subjects.append(subject.Subject.name)

        temp = display_grades(self.logged_user_id, "Student")
        self.subjects_name = []
        self.grades = []

        for grade in temp:
            if grade.Subject.name in self.subjects_name:
                self.grades[self.subjects_name.index(grade.Subject.name)].append(grade.Grade.value)
            else:
                self.subjects_name.append(grade.Subject.name)
                tmp = [grade.Grade.value]
                self.grades.append(tmp)

        self.fill_table()

        # dodawanie obiektow
        logout_button = wx.Button(self, label="Logout", size=(100, 50))
        logout_button.SetBackgroundColour('orange')
        change_password_button = wx.Button(self, label="Change Password", size=(100, 50))
        change_password_button.SetBackgroundColour('pink')
        refresh_button = wx.Button(self, label="Refresh", size=(100, 50))
        refresh_button.SetBackgroundColour('green')

        # akcje obiektorw
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)
        refresh_button.Bind(wx.EVT_BUTTON, self.on_press_refresh)

        # rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, pos=(1, 1), flag=wx.EXPAND | wx.ALL)
        main_sizer.Add(change_password_button, pos=(1, 3))
        main_sizer.Add(logout_button, pos=(1, 4))
        main_sizer.Add(refresh_button, pos=(1, 2))

        self.SetSizer(main_sizer)

    def on_press_refresh(self, evt):
        print("UPDATE")
        self.fill_table()

    def on_press_chngpass(self, event):
        changePasswordFrame(self.logged_user_id)

    def on_press_logout(self, event):
        exit()

    def fill_table(self):
        # czyszczenie tablicy
        self.list_ctrl.DeleteAllItems()
        # wypelnianie tablicy
        row = 0
        for subject in self.subjects_name:
            self.list_ctrl.InsertItem(row, subject)  # gdzie 0 to indeks wiersza
            index = 0
            for grade in self.grades[row]:
                self.list_ctrl.SetItem(row, index+1, str(grade))  # gdzie index to indeks kolumny a str(index) to wartość(ocena)
                index += 1
            row += 1


class studentFrame(wx.Frame):
    def __init__(self, logged_user):
        super().__init__(parent=None, title="elearning Student")
        self.SetSize(1440, 720)
        self.panel = studentPanel(self, logged_user=logged_user)
        self.Show()
