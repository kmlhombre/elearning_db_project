import wx

from addGradeWindow import addGradeFrame
from changePasswordWindow import changePasswordFrame

from methods import get_subjects, get_students, get_grades_of_student, get_subject_id


class teacherPanel(wx.Panel):

    def __init__(self, parent, logged_user):
        super().__init__(parent)
        main_sizer = wx.GridBagSizer(10, 10)
        self.row_obj_dict = {}
        self.current_folder_path = None

        self.logged_user_id = logged_user

        # stworzenie tabeli
        self.list_ctrl = wx.ListCtrl(self, size=(700, 600), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, "Subject", width=140)
        self.list_ctrl.SetColumnWidth(0, 120)
        self.list_ctrl.SetScrollbar(wx.HORIZONTAL, 0, 16, 50)
        for index in range(1, 50):
            self.list_ctrl.InsertColumn(index, "Grade", width=60)
            self.list_ctrl.SetColumnWidth(index, 60)

        #TODO tutaj funkcja ktora pobiera dane tj.
        #przedmioty
        self.subjects = []
        sub_tmp = get_subjects()
        for subject in sub_tmp:
            self.subjects.append(subject.Subject.name + ' ' + subject.Class.name)

        #uczniow i oceny pierwszego przedmiotu
        self.students = []
        self.student_grades_class_subject = None

        self.students_id = []
        self.grades = []
        self.student_data = []

        # dodawanie obiektow
        logout_button = wx.Button(self, label="Logout", size=(100, 50))
        logout_button.SetBackgroundColour('orange')
        self.subject_choice = wx.Choice(self, choices=self.subjects, size=(100, 100))
        change_password_button = wx.Button(self, label="Change Password", size=(100, 50))
        change_password_button.SetBackgroundColour('pink')
        add_grade_button = wx.Button(self, label="Add Grade", size=(100, 50))
        add_grade_button.SetBackgroundColour(wx.Colour(137, 207, 240))

        # akcje obiektorw
        self.subject_choice.SetSelection(0)
        self.subject_choice.Bind(wx.EVT_CHOICE, self.on_choice)
        add_grade_button.Bind(wx.EVT_BUTTON, self.on_add_grade)
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        #uzupelnianie tabeli danymi z pierwszego przedmiotu
        self.fill_table(subject=self.subjects[self.subject_choice.GetCurrentSelection()])

        # rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, pos=(1, 1), flag = wx.EXPAND|wx.ALL)
        main_sizer.Add(change_password_button, pos=(1, 4))
        main_sizer.Add(add_grade_button, pos=(1, 3))
        main_sizer.Add(self.subject_choice, pos=(1, 2))
        main_sizer.Add(logout_button, pos=(1, 5))

        self.SetSizer(main_sizer)

    def on_choice(self, event):
        print(self.subjects[self.subject_choice.GetCurrentSelection()]) #wyswietla wybrany przedmiot
        self.fill_table(subject=self.subjects[self.subject_choice.GetCurrentSelection()]) #wypelnia na nowo tabele nowo pobranymi danymi

    def on_press_chngpass(self, event):
        changePasswordFrame(self.logged_user_id)

    def on_press_logout(self, event):
        exit()

    def on_add_grade(self, event):
        subject_tmp = self.subjects[self.subject_choice.GetCurrentSelection()].split(' ')
        s = ' '.join(subject_tmp[:-2])
        c = ' '.join(subject_tmp[-2:])
        sub_id = get_subject_id(s, c)

        addGradeFrame(students=self.students, subject=sub_id.subject_id)
        self.fill_table(self.subjects[self.subject_choice.GetCurrentSelection()]) #odswiezenie tablicy

    def fill_table(self, subject):
        # TODO tutaj pobiera uczniow i oceny z wybranego przedmiotu i odswieza tabele
        subject_tmp = subject.split(' ')
        s = ' '.join(subject_tmp[:-2])
        c = ' '.join(subject_tmp[-2:])
        self.students.clear()
        self.students_id.clear()
        self.student_data.clear()

        self.student_grades_class_subject = get_students(s, c)

        '''for student in self.student_grades_class_subject:
            if student.student_id in self.students_id:
                self.grades[self.students_id.index(student.Student.student_id)].append(student.Grade.value)
            else:
                self.students_id.append(student.student_id)
                self.student_data.append(student.first_name + ' ' + student.surname)
                tmp = [student.value]
                self.grades.append(tmp)
                self.grades[self.students_id.index(student.student_id)].append(student.value - 1)'''
        # czyszczenie tablicy
        self.list_ctrl.DeleteAllItems()

        row = 0
        sub_id = get_subject_id(s, c)
        print(self.student_grades_class_subject)
        for student in self.student_grades_class_subject:
            index = 0
            s_temp = get_grades_of_student(sub_id.subject_id, student.student_id)
            self.students.append([student.student_id, student.first_name, student.surname])
            self.list_ctrl.InsertItem(row, (student.first_name + ' ' + student.surname))
            for grade in s_temp:
                self.list_ctrl.SetItem(row, index+1, str(grade.value))
                index += 1
            row += 1
        #wypelnianie tablicy
        '''row = 0
        for i in range(len(self.students_id)):
            self.list_ctrl.InsertItem(i, self.student_data[i])
            index = 0
            for grade in self.grades[i]:
                self.list_ctrl.SetItem(i, index+1, str(grade))
                index += 1'''
        """for student in self.student_data:
            self.list_ctrl.InsertItem(row, student)
            index = 0
            for grade in self.grades[row]:
                self.list_ctrl.SetItem(row, index+1, str(grade))
                index += 1
            row += 1
"""
class teacherFrame(wx.Frame):
    def __init__(self, logged_user):
        super().__init__(parent=None, title="elearning Teacher")
        self.SetSize(1280, 720)
        self.panel = teacherPanel(self, logged_user=logged_user)
        self.Show()
