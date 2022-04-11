# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YTDownloader.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 450)
        MainWindow.setMinimumSize(QSize(20, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 370, 261, 21))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(124, 113, 116);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(59, 59, 59, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 220, 136, 19))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 140, 169, 47))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pathLabel = QLabel(self.widget1)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pathLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pathLabel, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 0))
        self.pushButton.setMaximumSize(QSize(75, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 0, 0);	\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(60, 270, 181, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.oneVideoButton = QPushButton(self.widget2)
        self.oneVideoButton.setObjectName(u"oneVideoButton")
        self.oneVideoButton.setMinimumSize(QSize(60, 0))
        self.oneVideoButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 7px;\n"
"	border-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.oneVideoButton)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(70, 0, 167, 122))
        self.verticalLayout = QVBoxLayout(self.widget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(130, 75))
        self.frame.setStyleSheet(u"image: url(:/youtubelogo/Youtube-logo-vector-PNG.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.TitleName_2 = QLabel(self.widget3)
        self.TitleName_2.setObjectName(u"TitleName_2")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.TitleName_2.setFont(font1)
        self.TitleName_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.TitleName_2.setAlignment(Qt.AlignCenter)
        self.TitleName_2.setMargin(10)

        self.verticalLayout.addWidget(self.TitleName_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YouTube Downloader", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"One video", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Path to save</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Enter path or choose", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Paste your link", None))
        self.oneVideoButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.TitleName_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Downloader</span></p></body></html>", None))
    # retranslateUi

