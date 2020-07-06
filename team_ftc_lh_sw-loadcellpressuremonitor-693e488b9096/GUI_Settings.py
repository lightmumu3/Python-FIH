# -*- coding: utf-8 -*-
import datetime
from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget
from mainUI import *
#from settingsUI import*
from TCPSocket import *
from setGPIO_mode import *
from load_setting_xml import *
import RPi.GPIO as GPIO
from PyQt5.QtCore import *

class GUI_Settings(QMainWindow, Ui_MainWindow):
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg = QtCore.pyqtSignal(str)
    sinOut = QtCore.pyqtSignal(str)

    sig_setting = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("LoadCellPressureMonitor_"+VERSION)
        self.connect()

    def connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        pass

if __name__ == '__main__':
    """
    显示界面
    """
    app = QApplication(sys.argv)
    ui = GUI_Settings()
    ui.show()
    sys.exit(app.exec_())
