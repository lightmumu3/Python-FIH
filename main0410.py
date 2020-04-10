# from PyQt5.QtWidgets import*
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#from calc_interface import Ui_MainWindow
import os,sys

import cal_UI0410      #调用ui
from logic0410 import *   #调用logic中定义的函数方法，没有的话会报错

# global e_view
# from PyQt5 import QtCore, QtGui, QtWidgets




if __name__ == '__main__':
 app=QApplication(sys.argv)
 myWin=MyMainWindow()
 myWin.show()
 sys.exit(app.exec())