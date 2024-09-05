#!../bin/python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from login import Ui_MainWindow
from Emp import Ui_mainWindow
from authentication import *
from operations import *
from Admin import Admin_mainWindow
from employee_data import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
login_ui = Ui_MainWindow()
Emp_ui = Ui_mainWindow()
Admin_ui = Admin_mainWindow()


TrialNumber = 2
Logged_ID = -1
Username = ""

def show_notification(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Close)
    msg.exec_()

def show_emp_info():
    Emp_ui.label.setText(display_info(Logged_ID))

def show_bonus():
    Emp_ui.label.setText(calculate_bonus(Logged_ID))

def show_disc():
    Emp_ui.label.setText(calculate_discount(Logged_ID))

def show_holidays():
    Emp_ui.label.setText(remind_legal_holidays(Logged_ID))

def app_exit():
    switch_window()

def DeletePlainTxt():
    Admin_ui.ID.clear()
    Admin_ui.Name.clear()
    Admin_ui.Depart.clear()
    Admin_ui.Salary.clear()
    Admin_ui.Days.clear()
    Admin_ui.Password.clear()


def Add_Data():
    if add_employee(Admin_ui.ID.toPlainText(),
                 Admin_ui.Name.toPlainText(),
                 Admin_ui.Depart.toPlainText(),
                 Admin_ui.Salary.toPlainText(),
                 Admin_ui.Password.text(),
                 Admin_ui.Days.toPlainText()) == False:
        Admin_ui.label.setText("Error check parameter")
    else:
        Admin_ui.label.setText("Done Adding New Employee")
        DeletePlainTxt()

def Delete_Data():
    if remove_employee(Admin_ui.ID.toPlainText()) == False:
        Admin_ui.label.setText("Error check ID")
    else:
        Admin_ui.label.setText("Done Removing Employee")
        DeletePlainTxt()

def Update_Data():
    if update_employee(Admin_ui.ID.toPlainText(),
                 Admin_ui.Name.toPlainText(),
                 Admin_ui.Depart.toPlainText(),
                 Admin_ui.Salary.toPlainText(),
                 Admin_ui.Password.text(),
                 Admin_ui.Days.toPlainText()) == False:
        Admin_ui.label.setText("Error check parameter")
    else:
        Admin_ui.label.setText("Done Updating Employee")
        DeletePlainTxt()

def Get_Data():
    Admin_ui.label.setText(display_info(Admin_ui.ID.toPlainText()))
    DeletePlainTxt()

def switch_window(toWhat='default'):
    MainWindow.close()
    if toWhat == "Emp":
        Emp_ui.setupUi(MainWindow)
        MainWindow.show()
        Emp_ui.Disp_info.clicked.connect(show_emp_info)
        Emp_ui.Bonus.clicked.connect(show_bonus)
        Emp_ui.Discount.clicked.connect(show_disc)
        Emp_ui.Holidays.clicked.connect(show_holidays)
        Emp_ui.Exit.clicked.connect(app_exit)
    elif toWhat == "Admin":
        Admin_ui.setupUi(MainWindow)
        MainWindow.show()
        Admin_ui.Add.clicked.connect(Add_Data)
        Admin_ui.Remove.clicked.connect(Delete_Data)
        Admin_ui.GetData.clicked.connect(Get_Data)
        Admin_ui.Update.clicked.connect(Update_Data)
        Admin_ui.Exit.clicked.connect(app_exit)
    else:
        login_ui.setupUi(MainWindow)
        MainWindow.show()
        login_ui.pushButton.clicked.connect(check_login)


def check_login():
    global TrialNumber
    global Logged_ID
    Logged_ID = login_ui.textEdit.toPlainText()
    login_res = login(Logged_ID, login_ui.lineEdit.text())
    if TrialNumber == 0:
        show_notification("You Excedded Your Trials")
        exit()
    if login_res == False:
        TrialNumber -=1
    elif login_res == "Admin" :
        switch_window("Admin")
    else:
        switch_window("Emp")
    print(TrialNumber)

if __name__ == "__main__":
    switch_window()
    sys.exit(app.exec_())
