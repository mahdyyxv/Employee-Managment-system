# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Admin_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(753, 231)
        mainWindow.setMinimumSize(QtCore.QSize(753, 231))
        mainWindow.setMaximumSize(QtCore.QSize(753, 231))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../UI/admin-panel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(10, 10, 171, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../UI/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add.setIcon(icon1)
        self.Add.setIconSize(QtCore.QSize(40, 40))
        self.Add.setObjectName("Add")
        self.Remove = QtWidgets.QPushButton(self.centralwidget)
        self.Remove.setGeometry(QtCore.QRect(10, 60, 171, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../UI/rejection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Remove.setIcon(icon2)
        self.Remove.setIconSize(QtCore.QSize(40, 40))
        self.Remove.setObjectName("Remove")
        self.Update = QtWidgets.QPushButton(self.centralwidget)
        self.Update.setGeometry(QtCore.QRect(10, 110, 171, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../UI/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Update.setIcon(icon3)
        self.Update.setIconSize(QtCore.QSize(40, 40))
        self.Update.setObjectName("Update")
        self.GetData = QtWidgets.QPushButton(self.centralwidget)
        self.GetData.setGeometry(QtCore.QRect(10, 160, 171, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../UI/data-collection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GetData.setIcon(icon4)
        self.GetData.setIconSize(QtCore.QSize(40, 40))
        self.GetData.setObjectName("GetData")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(710, 60, 41, 81))
        self.Exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Exit.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../UI/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon5)
        self.Exit.setIconSize(QtCore.QSize(41, 81))
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 10, 261, 191))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(230, 3, 171, 31))
        self.ID.setObjectName("ID")
        self.Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(230, 37, 171, 31))
        self.Name.setObjectName("Name")
        self.Depart = QtWidgets.QTextEdit(self.centralwidget)
        self.Depart.setGeometry(QtCore.QRect(230, 71, 171, 31))
        self.Depart.setObjectName("Depart")
        self.Salary = QtWidgets.QTextEdit(self.centralwidget)
        self.Salary.setGeometry(QtCore.QRect(230, 103, 171, 31))
        self.Salary.setObjectName("Salary")
        self.Days = QtWidgets.QTextEdit(self.centralwidget)
        self.Days.setGeometry(QtCore.QRect(230, 136, 171, 31))
        self.Days.setObjectName("Days")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(230, 170, 171, 31))
        self.Password.setInputMask("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Admin Dashboard"))
        self.Add.setText(_translate("mainWindow", "Add Employee"))
        self.Remove.setText(_translate("mainWindow", "          Remove"))
        self.Update.setText(_translate("mainWindow", "            Update"))
        self.GetData.setText(_translate("mainWindow", "         Get Data"))
        self.ID.setPlaceholderText(_translate("mainWindow", "Employee ID"))
        self.Name.setPlaceholderText(_translate("mainWindow", "Employee Name"))
        self.Depart.setPlaceholderText(_translate("mainWindow", "Employee Department"))
        self.Salary.setPlaceholderText(_translate("mainWindow", "Employee Salary"))
        self.Days.setPlaceholderText(_translate("mainWindow", "Absence Days"))
        self.Password.setPlaceholderText(_translate("mainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Admin_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
