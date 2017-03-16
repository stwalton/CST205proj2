# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_2_redone.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MoneyApp(object):
    def setupUi(self, MoneyApp):
        MoneyApp.setObjectName("MoneyApp")
        MoneyApp.resize(307, 537)
        self.centralwidget = QtWidgets.QWidget(MoneyApp)
        self.centralwidget.setObjectName("centralwidget")
        self.Calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Calendar.setGeometry(QtCore.QRect(0, 30, 296, 183))
        self.Calendar.setObjectName("Calendar")
        self.Calendar.clicked.connect(self.calendar) #callendar click; goes to calendar function
        select_date = self.Calendar.selectedDate() #select_date is a variable thats holds the date from the calendar
        #help(select_date)
        select_date = select_date.toJulianDay()
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 0, 261, 31))
        self.text_1.setObjectName("text_1")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(10, 260, 291, 16))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(40, 340, 201, 20))
        self.text_4.setObjectName("text_4")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(20, 390, 271, 16))
        self.text_5.setObjectName("text_5")
        self.percent_value = QtWidgets.QSpinBox(self.centralwidget)
        self.percent_value.setGeometry(QtCore.QRect(100, 430, 62, 22))
        self.percent_value.setObjectName("percent_value")
        self.text_52 = QtWidgets.QLabel(self.centralwidget)
        self.text_52.setGeometry(QtCore.QRect(30, 410, 161, 16))
        self.text_52.setObjectName("text_52")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(50, 210, 201, 16))
        self.text_2.setObjectName("text_2")
        self.text_32 = QtWidgets.QLabel(self.centralwidget)
        self.text_32.setGeometry(QtCore.QRect(20, 280, 251, 16))
        self.text_32.setObjectName("text_32")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(100, 470, 75, 23))
        self.calculate_button.setObjectName("Calulate_button")
        self.save_value = QtWidgets.QTextEdit(self.centralwidget)
        self.save_value.setGeometry(QtCore.QRect(90, 230, 91, 31))
        self.save_value.setObjectName("save_value")
        self.startmn_value = QtWidgets.QTextEdit(self.centralwidget)
        self.startmn_value.setGeometry(QtCore.QRect(90, 300, 91, 31))
        self.startmn_value.setObjectName("startmn_value")
        self.paycheck_value = QtWidgets.QTextEdit(self.centralwidget)
        self.paycheck_value.setGeometry(QtCore.QRect(90, 360, 91, 31))
        self.paycheck_value.setObjectName("paycheck_value")
        MoneyApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoneyApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 307, 21))
        self.menubar.setObjectName("menubar")
        self.File_menu = QtWidgets.QMenu(self.menubar)
        self.File_menu.setObjectName("File_menu")
        self.Export = QtWidgets.QMenu(self.menubar)
        self.Export.setObjectName("Export")
        MoneyApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MoneyApp)
        self.statusbar.setObjectName("statusbar")
        MoneyApp.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MoneyApp)
        self.actionOpen.setObjectName("actionOpen")
        self.exit = QtWidgets.QAction(MoneyApp)
        self.exit.setObjectName("exit")
        self.new_2 = QtWidgets.QAction(MoneyApp)
        self.new_2.setObjectName("new_2")
        self.txt_export = QtWidgets.QAction(MoneyApp)
        self.txt_export.setObjectName("txt_export")
        self.File_menu.addAction(self.new_2)
        self.File_menu.addAction(self.exit)
        self.Export.addAction(self.txt_export)
        self.menubar.addAction(self.File_menu.menuAction())
        self.menubar.addAction(self.Export.menuAction())

        self.retranslateUi(MoneyApp)
        QtCore.QMetaObject.connectSlotsByName(MoneyApp)

    def retranslateUi(self, MoneyApp):
        _translate = QtCore.QCoreApplication.translate
        MoneyApp.setWindowTitle(_translate("MoneyApp", "Money Well Saved"))
        self.text_1.setText(_translate("MoneyApp", "1. Select a date you wish have your money save by."))
        self.text_3.setText(_translate("MoneyApp", "3. How much money do you have already started to save?"))
        self.text_4.setText(_translate("MoneyApp", "4. How much do you make per paycheck?"))
        self.text_5.setText(_translate("MoneyApp", "5. How much do you want to take out of your paycheck"))
        self.text_52.setText(_translate("MoneyApp", "Please select how much percent"))
        self.text_2.setText(_translate("MoneyApp", "2. How much do you need to save?"))
        self.text_32.setText(_translate("MoneyApp", "You can enter in 0 if you dont have money saved."))
        self.calculate_button.setText(_translate("MoneyApp", "Calculate"))
        self.calculate_button.clicked.connect(self.calculate) #calculate button; goes to calculate function
        self.File_menu.setTitle(_translate("MoneyApp", "File"))
        self.Export.setTitle(_translate("MoneyApp", "Export"))
        self.actionOpen.setText(_translate("MoneyApp", "Open"))
        self.exit.setText(_translate("MoneyApp", "Exit"))
        self.new_2.setText(_translate("MoneyApp", "New"))
        self.txt_export.setText(_translate("MoneyApp", ".txt"))

    def calendar(self, select_date):
        print(select_date)

    def calculate(self):
        tax = (self.percent_value.value()) #Tax variable/value
        save = float(self.save_value.toPlainText()) #save variable/value
        start_amount = float(self.startmn_value.toPlainText()) #start amount variable/value
        paycheck = float(self.paycheck_value.toPlainText()) #paycheck amount variable/value
        print("It worked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoneyApp = QtWidgets.QMainWindow()
    ui = Ui_MoneyApp()
    ui.setupUi(MoneyApp)
    MoneyApp.show()
    sys.exit(app.exec_())

