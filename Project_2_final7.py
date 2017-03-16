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
        self.cal_day = 0 #Gets the day when you click the calendar. Changes in the calendar function
        self.cal_month = 0 #Gets the month when you click the calendar. Changes in the calendar function
        self.cal_year = 0 #Gets the year when you click the calendar. Changes in the calendar function
        self.cur_day = 0 #Intializes curent day. Changes in the calculate function
        self.cur_month = 0 #Intializes curent month. Changes in the calculate function
        self.cur_year = 0 #Intializes curent year. Changes in the calculate function
        self.tax = 0 #Intializes variable tax. Changes in the calculate function
        self.save = 0 #intializes save variable for the current save box. Changes value in the calculate function
        self.start_amount = 0 #intializes starting amount variable. Changes value in the calculate function
        self.paycheck = 0 #Initializes paycheck variable. Changes in the calculate function.
        self.total_days = 0 #Initializes total days variable. This will store the total days from julian day formula.
        self.calculation1 = 0 #Initalizes the first calculation that will be printed
        self.calculation2 = 0 #Initalizes the second calculation that will be printed
        self.tax2 = 0 #Initializes tax2, as it needs to be turned into a decimal to calculate how much percent from income to take out 
        
        #The Main Window
        MoneyApp.setObjectName("MoneyApp") #Name of main window
        MoneyApp.resize(308, 650) #Size of main window
        
        self.centralwidget = QtWidgets.QWidget(MoneyApp)
        self.centralwidget.setObjectName("centralwidget")
        #Calendar Widget
        self.Calendar = QtWidgets.QCalendarWidget(self.centralwidget) 
        self.Calendar.setGeometry(QtCore.QRect(0, 30, 296, 183)) #Widget size
        self.Calendar.setObjectName("Calendar")
        #Calendar click; goes to calendar function
        self.Calendar.clicked.connect(self.calendar) 
        #Text that is above the calendar
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 0, 261, 31))
        self.text_1.setObjectName("text_1")
        #Text for instruction 3
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(10, 270, 291, 20))
        self.text_3.setObjectName("text_3")
        #Text for weekly income box
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(10, 340, 231, 20))
        self.text_4.setObjectName("text_4")
        #Text for Percent box
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(20, 390, 271, 16))
        self.text_5.setObjectName("text_5")
        #Box to select percent value
        self.percent_value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.percent_value.setGeometry(QtCore.QRect(110, 430, 62, 22))
        self.percent_value.setObjectName("percent_value")
        #Extended text for instruction 5
        self.text_52 = QtWidgets.QLabel(self.centralwidget)
        self.text_52.setGeometry(QtCore.QRect(70, 410, 161, 16))
        self.text_52.setObjectName("text_52")
        #Text for how much the user needs to save
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(60, 220, 201, 16))
        self.text_2.setObjectName("text_2")
        #Extended text for instruction 3
        self.text_32 = QtWidgets.QLabel(self.centralwidget)
        self.text_32.setGeometry(QtCore.QRect(10, 290, 281, 20))
        self.text_32.setObjectName("text_32")
        #Input box for user to type in how much they need to save
        self.save_value = QtWidgets.QTextEdit(self.centralwidget)
        self.save_value.setGeometry(QtCore.QRect(100, 240, 91, 31))
        self.save_value.setObjectName("save_value")
        #Input box for user to type in how much money they might of started saving
        self.startmn_value = QtWidgets.QTextEdit(self.centralwidget)
        self.startmn_value.setGeometry(QtCore.QRect(100, 310, 91, 31))
        self.startmn_value.setObjectName("startmn_value")
        #Input box for weekly income 
        self.paycheck_value = QtWidgets.QTextEdit(self.centralwidget)
        self.paycheck_value.setGeometry(QtCore.QRect(100, 360, 91, 31))
        self.paycheck_value.setObjectName("paycheck_value")
        #Text for Calculate button
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 261, 20))
        self.label.setObjectName("label")
        #The calculation button - The one button to rule them all
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(110, 500, 61, 23))
        self.calculate_button.setObjectName("calculate")
        #Additional text for the calculate button
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 480, 171, 20))
        self.label_2.setObjectName("label_2")
        #Display text after you hit calculate
        self.final_text1 = QtWidgets.QLabel(self.centralwidget)
        self.final_text1.setGeometry(QtCore.QRect(10, 530, 291, 20))
        self.final_text1.setObjectName("final_text1")
        #Same as above
        self.final_text2 = QtWidgets.QLabel(self.centralwidget)
        self.final_text2.setGeometry(QtCore.QRect(10, 550, 291, 20))
        self.final_text2.setObjectName("final_text2")
        #Same as above
        self.final_text3 = QtWidgets.QLabel(self.centralwidget)
        self.final_text3.setGeometry(QtCore.QRect(10, 570, 291, 20))
        self.final_text3.setObjectName("final_text3")
        #Same as above
        self.final_text4 = QtWidgets.QLabel(self.centralwidget)
        self.final_text4.setGeometry(QtCore.QRect(6, 590, 301, 20))
        self.final_text4.setObjectName("final_text4")

        MoneyApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoneyApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName("menubar")
        #File drop down menu on top of window
        self.File_menu = QtWidgets.QMenu(self.menubar)
        self.File_menu.setObjectName("File_menu")
        #Export drop down menu next to the File drop down menu
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
        #This sets the name for the window
        MoneyApp.setWindowTitle(_translate("MoneyApp", "Money Well Saved"))
        #Text for self.text_1
        self.text_1.setText(_translate("MoneyApp", "1. Select a date you wish have your money save by."))
        #Text for self.text_3
        self.text_3.setText(_translate("MoneyApp", "3. This will calculate how many day\'s it will take to save. "))
        #Text for self.text_4
        self.text_4.setText(_translate("MoneyApp", "4. Please enter in how much you make a week."))
        #Text for self.text_5
        self.text_5.setText(_translate("MoneyApp", "5. How much do you want to take out of your paycheck"))
        #Text for self.text_52
        self.text_52.setText(_translate("MoneyApp", "Please select how much percent"))
        #Text for self.text_2
        self.text_2.setText(_translate("MoneyApp", "2. How much do you need to save?"))
        #Text for self.text_32
        self.text_32.setText(_translate("MoneyApp", "Enter in how much money you saved already."))
        self.label.setText(_translate("MoneyApp", "6. Hit calculate to see how much you need to save."))
        self.calculate_button.setText(_translate("MoneyApp", "Calculate"))
        #calculate button; goes to calculate function
        self.calculate_button.clicked.connect(self.calculate)
        #Text before the button
        self.label_2.setText(_translate("MoneyApp", "It will the calculation below."))
        #These are the output for the calculations. They are set in the calculation function
        self.final_text1.setText(_translate("MoneyApp", ""))
        self.final_text2.setText(_translate("MoneyApp", ""))
        self.final_text3.setText(_translate("MoneyApp", ""))
        self.final_text4.setText(_translate("MoneyApp", ""))
        self.File_menu.setTitle(_translate("MoneyApp", "File"))
        #Drop down menu items
        self.Export.setTitle(_translate("MoneyApp", "Export"))
        self.actionOpen.setText(_translate("MoneyApp", "Open"))
        self.exit.setText(_translate("MoneyApp", "Exit"))
        self.new_2.setText(_translate("MoneyApp", "New"))
        self.txt_export.setText(_translate("MoneyApp", ".txt"))

    # When you click the calendar, this function runs. This function is need to store the dates
    def calendar(self, select_date):
        
        print(select_date.toJulianDay())
        self.cal_day = (select_date.day())#store the day from the calendar
        self.cal_month = (select_date.month()) #stores the month from the calendar
        self.cal_year = (select_date.year()) #stores the year from the calendar


    # When you click calculate, this function runs. Calculates and displays how much you need to save
    def calculate(self):
        # help(self.Calendar)#.getSelectedDate()
        
        self.tax = float(self.percent_value.value()) #Tax variable/value
        self.save = float(self.save_value.toPlainText()) #save variable/value
        self.start_amount = float(self.startmn_value.toPlainText()) #start amount variable/value
        self.paycheck = float(self.paycheck_value.toPlainText()) #paycheck amount variable/value
        
        cur_d = QtCore.QDate.currentDate() # calls for current date
        self.cur_day = (cur_d.day()) # stores current day
        self.cur_month = (cur_d.month()) #stores current month
        self.cur_year = (cur_d.year()) #stores current year
    
        import math #need this so I can accuratly print out the day with no decimal. Used math.ceil
        
        # Julian Day formula to see how many days have passed
        if self.cur_month < 3:
            self.cur_year = self.cur_year - 1
            self.cur_month += 12

        if self.cal_month < 3:
            self.cal_year = self.cur_year - 1
            self.cal_month += 12
        
        calc1 = (365 * self.cur_year) + (self.cur_year / 4) - (self.cur_year / 100) + (self.cur_year / 400) + (153 * self.cur_month - 457) / 5 + self.cur_day - 306 
        calc2 = (365 * self.cal_year) + (self.cal_year / 4) - (self.cal_year / 100) + (self.cal_year / 400) + (153 * self.cal_month - 457) / 5 + self.cal_day - 306
        self.total_days = calc2 - calc1
        self.total_days = math.ceil(self.total_days) #this remove the decimals 

        self.tax2 = self.tax / 100
        self.calculation1 = self.save / self.total_days
        self.calculation1 = round(self.calculation1, 2)
        quick_math1 = self.save - self.start_amount
        quick_math2 = self.paycheck * self.tax2
        self.calculation2 = (quick_math1 / quick_math2) * 7
        self.calculation2 = math.ceil(self.calculation2) #this is to remove decimals
        #These are string variables which are set to display in the final_text dialog 
        calculation1_string = "You need to save " +  str(self.calculation1) + " for the next "  + str(self.total_days) + " days."
        calculation2_string = "With your weekly income at " + str(self.paycheck) + " with " + str(self.tax) + "% going"
        calculation3_string = "toward savings, it would take " + str(self.calculation2) + " days to achieve"
        calculation4_string = "your goal. The amount taken out of your income is: " + str(quick_math2)
        self.final_text1.setText(calculation1_string)
        self.final_text2.setText(calculation2_string)
        self.final_text3.setText(calculation3_string)
        self.final_text4.setText(calculation4_string)

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoneyApp = QtWidgets.QMainWindow()
    ui = Ui_MoneyApp()
    ui.setupUi(MoneyApp)
    MoneyApp.show()
    sys.exit(app.exec_())

