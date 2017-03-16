# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_2_final.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MoneyApp(object):
    def setupUi(self, MoneyApp):
        #This is so I can pass the variables through different functions if I need to. Also this is all the variables.
        self.cal_day = 0; #Gets the day when you click the calendar. Changes in the calendar function
        self.cal_month = 0; #Gets the month when you click the calendar. Changes in the calendar function
        self.cal_year = 0; #Gets the year when you click the calendar. Changes in the calendar function
        self.cur_day = 0; #Intializes curent day. Changes in the calculate function
        self.cur_month = 0; #Intializes curent month. Changes in the calculate function
        self.cur_year = 0; #Intializes curent year. Changes in the calculate function
        self.tax = 0; #Intializes variable tax. Changes in the calculate function
        self.save = 0; #intializes save variable for the current save box. Changes value in the calculate function
        self.start_amount = 0; #intializes starting amount variable. Changes value in the calculate function
        self.paycheck = 0; #Initializes paycheck variable. Changes in the calculate function.
        
        MoneyApp.setObjectName("MoneyApp")
        MoneyApp.resize(308, 645)
        
        self.centralwidget = QtWidgets.QWidget(MoneyApp)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Calendar.setGeometry(QtCore.QRect(0, 30, 296, 183))
        self.Calendar.setObjectName("Calendar")
        self.Calendar.clicked.connect(self.calendar) #callendar click; goes to calendar function
        
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 0, 261, 31))
        self.text_1.setObjectName("text_1")

        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(10, 270, 291, 20))
        self.text_3.setObjectName("text_3")

        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(10, 340, 231, 20))
        self.text_4.setObjectName("text_4")

        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(20, 390, 271, 16))
        self.text_5.setObjectName("text_5")

        self.percent_value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.percent_value.setGeometry(QtCore.QRect(110, 430, 62, 22))
        self.percent_value.setObjectName("percent_value")

        self.text_52 = QtWidgets.QLabel(self.centralwidget)
        self.text_52.setGeometry(QtCore.QRect(70, 410, 161, 16))
        self.text_52.setObjectName("text_52")

        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(60, 220, 201, 16))
        self.text_2.setObjectName("text_2")

        self.text_32 = QtWidgets.QLabel(self.centralwidget)
        self.text_32.setGeometry(QtCore.QRect(10, 290, 281, 20))
        self.text_32.setObjectName("text_32")

        self.save_value = QtWidgets.QTextEdit(self.centralwidget)
        self.save_value.setGeometry(QtCore.QRect(100, 240, 91, 31))
        self.save_value.setObjectName("save_value")

        self.startmn_value = QtWidgets.QTextEdit(self.centralwidget)
        self.startmn_value.setGeometry(QtCore.QRect(100, 310, 91, 31))
        self.startmn_value.setObjectName("startmn_value")

        self.paycheck_value = QtWidgets.QTextEdit(self.centralwidget)
        self.paycheck_value.setGeometry(QtCore.QRect(100, 360, 91, 31))
        self.paycheck_value.setObjectName("paycheck_value")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 261, 20))
        self.label.setObjectName("label")

        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(110, 500, 61, 23))
        self.calculate_button.setObjectName("calculate")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 480, 171, 20))
        self.label_2.setObjectName("label_2")

        self.calc_display = QtWidgets.QTextEdit(self.centralwidget)
        self.calc_display.setGeometry(QtCore.QRect(10, 530, 291, 71))
        self.calc_display.setObjectName("calc_display")

        MoneyApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoneyApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
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
        self.text_3.setText(_translate("MoneyApp", "3. This will calculate how many day\'s it will take to save. "))
        self.text_4.setText(_translate("MoneyApp", "4. Please enter in how much you make a week."))
        self.text_5.setText(_translate("MoneyApp", "5. How much do you want to take out of your paycheck"))
        self.text_52.setText(_translate("MoneyApp", "Please select how much percent"))
        self.text_2.setText(_translate("MoneyApp", "2. How much do you need to save?"))
        self.text_32.setText(_translate("MoneyApp", "Enter in how much money you saved already."))
        self.label.setText(_translate("MoneyApp", "6. Hit calculate to see how much you need to save."))
        self.calculate_button.setText(_translate("MoneyApp", "Calculate"))
        self.calculate_button.clicked.connect(self.calculate) #calculate button; goes to calculate function
        self.label_2.setText(_translate("MoneyApp", "It will the calculation below."))
        self.File_menu.setTitle(_translate("MoneyApp", "File"))
        self.Export.setTitle(_translate("MoneyApp", "Export"))
        self.actionOpen.setText(_translate("MoneyApp", "Open"))
        self.exit.setText(_translate("MoneyApp", "Exit"))
        self.new_2.setText(_translate("MoneyApp", "New"))
        self.txt_export.setText(_translate("MoneyApp", ".txt"))

    # When you click the callendar, this function runs. This function is need to store the dates
    def calendar(self, select_date):
        print(select_date.toJulianDay())
        self.cal_day = (select_date.day())#store the day from the calendar
        self.cal_month = (select_date.month()) #stores the month from the calendar
        self.cal_year = (select_date.year()) #stores the year from the calendar


    # When you click calculate, this function runs. Calculates and displays how much you need to save
    def calculate(self):
        # help(self.Calendar)#.getSelectedDate()
        
        self.tax = (self.percent_value.value()) #Tax variable/value
        self.save = (self.save_value.toPlainText()) #save variable/value
        self.start_amount = (self.startmn_value.toPlainText()) #start amount variable/value
        self.paycheck = (self.paycheck_value.toPlainText()) #paycheck amount variable/value
        
        cur_d = QtCore.QDate.currentDate() # calls for current date
        self.cur_day = (cur_d.day()) # stores current day
        self.cur_month = (cur_d.month()) #stores current month
        self.cur_year = (cur_d.year()) #stores current year
      
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoneyApp = QtWidgets.QMainWindow()
    ui = Ui_MoneyApp()
    ui.setupUi(MoneyApp)
    MoneyApp.show()
    sys.exit(app.exec_())

