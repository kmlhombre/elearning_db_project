import wx

from gui.changePasswordWindow import changePasswordFrame

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

        # TODO tutaj funkcja ktora pobiera dane tj.
        # przedmioty
        # uczniow i oceny pierwszego przedmiotu

        self.subjects = ["Math", "IT", "..."]

        # dodawanie obiektow
        logout_button = wx.Button(self, label="Logout", size=(100, 50))
        logout_button.SetBackgroundColour('orange')
        change_password_button = wx.Button(self, label="Change Password", size=(100, 50))
        change_password_button.SetBackgroundColour('pink')

        # akcje obiektorw
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        # rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, pos=(1, 1), flag=wx.EXPAND | wx.ALL)
        main_sizer.Add(change_password_button, pos=(1, 2))
        main_sizer.Add(logout_button, pos=(1, 3))

        self.SetSizer(main_sizer)

    def on_press_chngpass(self, event):
        changePasswordFrame(self.logged_user_id)

    def on_press_logout(self, event):
        exit()

    def fill_table(self, subject):
        # TODO tutaj pobiera uczniow i oceny z wybranego przedmiotu i odswieza tabele
        # czyszczenie tablicy
        self.list_ctrl.DeleteAllItems()
        # wypelnianie tablicy
        self.list_ctrl.InsertItem(0, "Math")  # gdzie 0 to indeks wiersza
        for index in range(1, 6):
            self.list_ctrl.SetItem(0, index, str(index))  # gdzie index to indeks kolumny a str(index) to wartość(ocena)


class studentFrame(wx.Frame):
    def __init__(self, logged_user):
        super().__init__(parent=None, title="elearning Student")
        self.SetSize(1280, 720)
        self.panel = studentPanel(self, logged_user=logged_user)
        self.Show()
