# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Emp.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(753, 231)
        mainWindow.setMinimumSize(QtCore.QSize(753, 231))
        mainWindow.setMaximumSize(QtCore.QSize(753, 231))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Disp_info = QtWidgets.QPushButton(self.centralwidget)
        self.Disp_info.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.Disp_info.setObjectName("Disp_info")
        self.Bonus = QtWidgets.QPushButton(self.centralwidget)
        self.Bonus.setGeometry(QtCore.QRect(10, 60, 171, 41))
        self.Bonus.setObjectName("Bonus")
        self.Discount = QtWidgets.QPushButton(self.centralwidget)
        self.Discount.setGeometry(QtCore.QRect(10, 110, 171, 41))
        self.Discount.setObjectName("Discount")
        self.Holidays = QtWidgets.QPushButton(self.centralwidget)
        self.Holidays.setGeometry(QtCore.QRect(10, 160, 171, 41))
        self.Holidays.setObjectName("Holidays")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(720, 14, 31, 181))
        self.Exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 491, 191))
        self.label.setMinimumSize(QtCore.QSize(491, 191))
        self.label.setMaximumSize(QtCore.QSize(491, 191))
        self.label.setText("")
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Emp. Managment System"))
        self.Disp_info.setText(_translate("mainWindow", "Display Emp. Inf."))
        self.Bonus.setText(_translate("mainWindow", "Calculate Bonus"))
        self.Discount.setText(_translate("mainWindow", "Calculate discount"))
        self.Holidays.setText(_translate("mainWindow", "Remind legal holidays"))
        self.Exit.setText(_translate("mainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
