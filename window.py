# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 241, 52, 255), stop:1 rgba(255, 111, 111, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_sup_serv = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sup_serv.setGeometry(QtCore.QRect(0, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn_sup_serv.setFont(font)
        self.btn_sup_serv.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.153409 rgba(85, 85, 255, 255), stop:1 rgba(255, 65, 0, 255));\n"
"border-radius: 30px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(255, 255, 0);")
        self.btn_sup_serv.setObjectName("btn_sup_serv")
        self.text_lang = QtWidgets.QLabel(self.centralwidget)
        self.text_lang.setGeometry(QtCore.QRect(330, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.text_lang.setFont(font)
        self.text_lang.setStyleSheet("background-color: rgb(255, 153, 64);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(0, 85, 127);\n"
"")
        self.text_lang.setObjectName("text_lang")
        self.choice_lang = QtWidgets.QComboBox(self.centralwidget)
        self.choice_lang.setGeometry(QtCore.QRect(560, 30, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.choice_lang.setFont(font)
        self.choice_lang.setStyleSheet("background-color: rgb(255, 153, 64);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(0, 85, 127);\n"
"")
        self.choice_lang.setMaxVisibleItems(10)
        self.choice_lang.setObjectName("choice_lang")
        self.choice_lang.addItem("")
        self.choice_lang.addItem("")
        self.choice_lang.addItem("")
        self.choice_lang.addItem("")
        self.btn_change_lang = QtWidgets.QPushButton(self.centralwidget)
        self.btn_change_lang.setGeometry(QtCore.QRect(820, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.btn_change_lang.setFont(font)
        self.btn_change_lang.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.153409 rgba(85, 85, 255, 255), stop:1 rgba(255, 65, 0, 255));\n"
"border-radius: 40px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(255, 255, 0);")
        self.btn_change_lang.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/button_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_change_lang.setIcon(icon)
        self.btn_change_lang.setIconSize(QtCore.QSize(64, 64))
        self.btn_change_lang.setObjectName("btn_change_lang")
        self.text_detail = QtWidgets.QLabel(self.centralwidget)
        self.text_detail.setGeometry(QtCore.QRect(0, 450, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.text_detail.setFont(font)
        self.text_detail.setStyleSheet("background-color: rgb(255, 153, 64);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(0, 85, 127);\n"
"")
        self.text_detail.setObjectName("text_detail")
        self.text_input = QtWidgets.QLabel(self.centralwidget)
        self.text_input.setGeometry(QtCore.QRect(0, 160, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.text_input.setFont(font)
        self.text_input.setStyleSheet("background-color: rgb(255, 153, 64);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(0, 85, 127);\n"
"")
        self.text_input.setObjectName("text_input")
        self.text_result = QtWidgets.QLabel(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(0, 320, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.text_result.setFont(font)
        self.text_result.setStyleSheet("background-color: rgb(255, 153, 64);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(0, 85, 127);\n"
"\n"
"")
        self.text_result.setObjectName("text_result")
        self.btn_comply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comply.setGeometry(QtCore.QRect(310, 250, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn_comply.setFont(font)
        self.btn_comply.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.153409 rgba(85, 85, 255, 255), stop:1 rgba(255, 65, 0, 255));\n"
"border-radius: 30px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(255, 255, 0);")
        self.btn_comply.setObjectName("btn_comply")
        self.input_data = QtWidgets.QTextEdit(self.centralwidget)
        self.input_data.setGeometry(QtCore.QRect(190, 160, 821, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_data.setFont(font)
        self.input_data.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);")
        self.input_data.setObjectName("input_data")
        self.input_detail = QtWidgets.QTextEdit(self.centralwidget)
        self.input_detail.setGeometry(QtCore.QRect(220, 450, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_detail.setFont(font)
        self.input_detail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);")
        self.input_detail.setObjectName("input_detail")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(190, 320, 821, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 5px solid rgb(0, 85, 127);")
        self.result.setObjectName("result")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(750, 250, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.153409 rgba(85, 85, 255, 255), stop:1 rgba(255, 65, 0, 255));\n"
"border-radius: 30px;\n"
"border: 5px solid rgb(0, 85, 127);\n"
"color: rgb(255, 255, 0);")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_sup_serv.setText(_translate("MainWindow", "Служба поддержки"))
        self.text_lang.setText(_translate("MainWindow", "Язык:"))
        self.choice_lang.setItemText(0, _translate("MainWindow", "Русский"))
        self.choice_lang.setItemText(1, _translate("MainWindow", "English"))
        self.choice_lang.setItemText(2, _translate("MainWindow", "中文"))
        self.choice_lang.setItemText(3, _translate("MainWindow", "Español"))
        self.text_detail.setText(_translate("MainWindow", "Точность:"))
        self.text_input.setText(_translate("MainWindow", "Ввод:"))
        self.text_result.setText(_translate("MainWindow", "Ответ:"))
        self.btn_comply.setText(_translate("MainWindow", "Выполнить"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
