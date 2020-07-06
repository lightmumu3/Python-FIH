# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 620)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet("")
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout_9.addWidget(self.btn_connect)
        self.txt_PSN = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.txt_PSN.setFont(font)
        self.txt_PSN.setObjectName("txt_PSN")
        self.horizontalLayout_9.addWidget(self.txt_PSN)
        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_setting.setObjectName("btn_setting")
        self.horizontalLayout_9.addWidget(self.btn_setting)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Sensor1_Alarm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sensor1_Alarm.sizePolicy().hasHeightForWidth())
        self.Sensor1_Alarm.setSizePolicy(sizePolicy)
        self.Sensor1_Alarm.setMinimumSize(QtCore.QSize(60, 60))
        self.Sensor1_Alarm.setAutoFillBackground(False)
        self.Sensor1_Alarm.setStyleSheet("border-image: url(:/image/Normal.jpg);\n"
"")
        self.Sensor1_Alarm.setObjectName("Sensor1_Alarm")
        self.horizontalLayout_2.addWidget(self.Sensor1_Alarm)
        self.txt_Sensor1Pressure = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor1Pressure.setFont(font)
        self.txt_Sensor1Pressure.setObjectName("txt_Sensor1Pressure")
        self.horizontalLayout_2.addWidget(self.txt_Sensor1Pressure)
        self.txt_Sensor1AlarmValue = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor1AlarmValue.setFont(font)
        self.txt_Sensor1AlarmValue.setObjectName("txt_Sensor1AlarmValue")
        self.horizontalLayout_2.addWidget(self.txt_Sensor1AlarmValue)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Sensor1_Alarm_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sensor1_Alarm_2.sizePolicy().hasHeightForWidth())
        self.Sensor1_Alarm_2.setSizePolicy(sizePolicy)
        self.Sensor1_Alarm_2.setMinimumSize(QtCore.QSize(60, 60))
        self.Sensor1_Alarm_2.setAutoFillBackground(False)
        self.Sensor1_Alarm_2.setStyleSheet("border-image: url(:/image/Normal.jpg);\n"
"")
        self.Sensor1_Alarm_2.setObjectName("Sensor1_Alarm_2")
        self.horizontalLayout_3.addWidget(self.Sensor1_Alarm_2)
        self.txt_Sensor2Pressure = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor2Pressure.setFont(font)
        self.txt_Sensor2Pressure.setObjectName("txt_Sensor2Pressure")
        self.horizontalLayout_3.addWidget(self.txt_Sensor2Pressure)
        self.txt_Sensor2AlarmValue = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor2AlarmValue.setFont(font)
        self.txt_Sensor2AlarmValue.setObjectName("txt_Sensor2AlarmValue")
        self.horizontalLayout_3.addWidget(self.txt_Sensor2AlarmValue)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Sensor1_Alarm_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sensor1_Alarm_3.sizePolicy().hasHeightForWidth())
        self.Sensor1_Alarm_3.setSizePolicy(sizePolicy)
        self.Sensor1_Alarm_3.setMinimumSize(QtCore.QSize(60, 60))
        self.Sensor1_Alarm_3.setAutoFillBackground(False)
        self.Sensor1_Alarm_3.setStyleSheet("border-image: url(:/image/Normal.jpg);\n"
"")
        self.Sensor1_Alarm_3.setObjectName("Sensor1_Alarm_3")
        self.horizontalLayout_4.addWidget(self.Sensor1_Alarm_3)
        self.txt_Sensor3Pressure = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor3Pressure.setFont(font)
        self.txt_Sensor3Pressure.setObjectName("txt_Sensor3Pressure")
        self.horizontalLayout_4.addWidget(self.txt_Sensor3Pressure)
        self.txt_Sensor3AlarmValue = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor3AlarmValue.setFont(font)
        self.txt_Sensor3AlarmValue.setObjectName("txt_Sensor3AlarmValue")
        self.horizontalLayout_4.addWidget(self.txt_Sensor3AlarmValue)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Sensor1_Alarm_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sensor1_Alarm_4.sizePolicy().hasHeightForWidth())
        self.Sensor1_Alarm_4.setSizePolicy(sizePolicy)
        self.Sensor1_Alarm_4.setMinimumSize(QtCore.QSize(60, 60))
        self.Sensor1_Alarm_4.setAutoFillBackground(False)
        self.Sensor1_Alarm_4.setStyleSheet("border-image: url(:/image/Normal.jpg);\n"
"")
        self.Sensor1_Alarm_4.setObjectName("Sensor1_Alarm_4")
        self.horizontalLayout_5.addWidget(self.Sensor1_Alarm_4)
        self.txt_Sensor4Pressure = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_Sensor4Pressure.sizePolicy().hasHeightForWidth())
        self.txt_Sensor4Pressure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor4Pressure.setFont(font)
        self.txt_Sensor4Pressure.setObjectName("txt_Sensor4Pressure")
        self.horizontalLayout_5.addWidget(self.txt_Sensor4Pressure)
        self.txt_Sensor4AlarmValue = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_Sensor4AlarmValue.setFont(font)
        self.txt_Sensor4AlarmValue.setObjectName("txt_Sensor4AlarmValue")
        self.horizontalLayout_5.addWidget(self.txt_Sensor4AlarmValue)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(60, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6.addWidget(self.frame)
        self.txt_TotalCount = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_TotalCount.setFont(font)
        self.txt_TotalCount.setObjectName("txt_TotalCount")
        self.horizontalLayout_6.addWidget(self.txt_TotalCount)
        self.txt_CurrentCount = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_CurrentCount.setFont(font)
        self.txt_CurrentCount.setObjectName("txt_CurrentCount")
        self.horizontalLayout_6.addWidget(self.txt_CurrentCount)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.txt_current_time = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.txt_current_time.setFont(font)
        self.txt_current_time.setObjectName("txt_current_time")
        self.horizontalLayout_8.addWidget(self.txt_current_time)
        self.txt_TimeAndIDAndIP = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.txt_TimeAndIDAndIP.setFont(font)
        self.txt_TimeAndIDAndIP.setObjectName("txt_TimeAndIDAndIP")
        self.horizontalLayout_8.addWidget(self.txt_TimeAndIDAndIP)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 18))
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
        self.btn_connect.setText(_translate("MainWindow", "連接"))
        self.txt_PSN.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PSN：</p></body></html>"))
        self.btn_setting.setText(_translate("MainWindow", "設定"))
        self.Sensor1_Alarm.setText(_translate("MainWindow", "1"))
        self.txt_Sensor1Pressure.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PV: </span></p></body></html>"))
        self.txt_Sensor1AlarmValue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">SV: </span></p></body></html>"))
        self.Sensor1_Alarm_2.setText(_translate("MainWindow", "2"))
        self.txt_Sensor2Pressure.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PV: </span></p></body></html>"))
        self.txt_Sensor2AlarmValue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">SV: </span></p></body></html>"))
        self.Sensor1_Alarm_3.setText(_translate("MainWindow", "3"))
        self.txt_Sensor3Pressure.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PV: </span></p></body></html>"))
        self.txt_Sensor3AlarmValue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">SV: </span></p></body></html>"))
        self.Sensor1_Alarm_4.setText(_translate("MainWindow", "4"))
        self.txt_Sensor4Pressure.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PV: </span></p></body></html>"))
        self.txt_Sensor4AlarmValue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">SV: </span></p></body></html>"))
        self.txt_TotalCount.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Total:</span></p></body></html>"))
        self.txt_CurrentCount.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Current:</span></p></body></html>"))
        self.txt_TimeAndIDAndIP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">ID:  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">IP:</span></p></body></html>"))
import image_rc
