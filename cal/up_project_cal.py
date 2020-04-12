'网上的计算器项目2020 4-9 下载'
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from calc_interface import Ui_MainWindow
import os,sys

global e_view      ###################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
 def setupUi(self, MainWindow):
  MainWindow.setObjectName("MainWindow")
  MainWindow.resize(647, 675)
  self.centralwidget = QtWidgets.QWidget(MainWindow)
  self.centralwidget.setObjectName("centralwidget")
  self.b_1 = QtWidgets.QPushButton(self.centralwidget)
  self.b_1.setGeometry(QtCore.QRect(10, 330, 71, 71))
  self.b_1.setObjectName("b_1")
  self.b_2 = QtWidgets.QPushButton(self.centralwidget)
  self.b_2.setGeometry(QtCore.QRect(80, 330, 71, 71))
  self.b_2.setObjectName("b_2")
  self.b_3 = QtWidgets.QPushButton(self.centralwidget)
  self.b_3.setGeometry(QtCore.QRect(150, 330, 71, 71))
  self.b_3.setObjectName("b_3")
  self.b_6 = QtWidgets.QPushButton(self.centralwidget)
  self.b_6.setGeometry(QtCore.QRect(150, 400, 71, 71))
  self.b_6.setObjectName("b_6")
  self.b_4 = QtWidgets.QPushButton(self.centralwidget)
  self.b_4.setGeometry(QtCore.QRect(10, 400, 71, 71))
  self.b_4.setObjectName("b_4")
  self.b_5 = QtWidgets.QPushButton(self.centralwidget)
  self.b_5.setGeometry(QtCore.QRect(80, 400, 71, 71))
  self.b_5.setObjectName("b_5")
  self.b_8 = QtWidgets.QPushButton(self.centralwidget)
  self.b_8.setGeometry(QtCore.QRect(80, 470, 71, 71))
  self.b_8.setObjectName("b_8")
  self.b_9 = QtWidgets.QPushButton(self.centralwidget)
  self.b_9.setGeometry(QtCore.QRect(150, 470, 71, 71))
  self.b_9.setObjectName("b_9")
  self.b_7 = QtWidgets.QPushButton(self.centralwidget)
  self.b_7.setGeometry(QtCore.QRect(10, 470, 71, 71))
  self.b_7.setObjectName("b_7")
  self.b_eq = QtWidgets.QPushButton(self.centralwidget)
  self.b_eq.setGeometry(QtCore.QRect(150, 540, 211, 71))
  self.b_eq.setObjectName("b_eq")
  self.b_mod = QtWidgets.QPushButton(self.centralwidget)
  self.b_mod.setGeometry(QtCore.QRect(220, 400, 71, 71))
  self.b_mod.setObjectName("b_mod")
  self.b_bra_l = QtWidgets.QPushButton(self.centralwidget)
  self.b_bra_l.setGeometry(QtCore.QRect(220, 330, 71, 71))
  self.b_bra_l.setObjectName("b_bra_l")
  self.b_div = QtWidgets.QPushButton(self.centralwidget)
  self.b_div.setGeometry(QtCore.QRect(220, 260, 71, 71))
  self.b_div.setObjectName("b_div")
  self.b_add = QtWidgets.QPushButton(self.centralwidget)
  self.b_add.setGeometry(QtCore.QRect(10, 260, 71, 71))
  self.b_add.setObjectName("b_add")
  self.b_sub = QtWidgets.QPushButton(self.centralwidget)
  self.b_sub.setGeometry(QtCore.QRect(80, 260, 71, 71))
  self.b_sub.setObjectName("b_sub")
  self.b_mul = QtWidgets.QPushButton(self.centralwidget)
  self.b_mul.setGeometry(QtCore.QRect(150, 260, 71, 71))
  self.b_mul.setObjectName("b_mul")
  self.b_pow = QtWidgets.QPushButton(self.centralwidget)
  self.b_pow.setGeometry(QtCore.QRect(290, 260, 71, 71))
  self.b_pow.setObjectName("b_pow")
  self.b_pai = QtWidgets.QPushButton(self.centralwidget)
  self.b_pai.setGeometry(QtCore.QRect(290, 400, 71, 71))
  self.b_pai.setObjectName("b_pai")
  self.b_bra_r = QtWidgets.QPushButton(self.centralwidget)
  self.b_bra_r.setGeometry(QtCore.QRect(290, 330, 71, 71))
  self.b_bra_r.setObjectName("b_bra_r")
  self.l_hist = QtWidgets.QListWidget(self.centralwidget)
  self.l_hist.setGeometry(QtCore.QRect(380, 10, 256, 601))
  self.l_hist.setObjectName("l_hist")
  self.e_view = QtWidgets.QTextEdit(self.centralwidget)
  self.e_view.setGeometry(QtCore.QRect(10, 10, 351, 231))
  font = QtGui.QFont()
  font.setFamily("Adobe Caslon Pro Bold")
  font.setPointSize(22)
  font.setBold(True)
  font.setWeight(75)
  self.e_view.setFont(font)                                ############################################
  self.e_view.setObjectName("e_view")
  self.b_0 = QtWidgets.QPushButton(self.centralwidget)
  self.b_0.setGeometry(QtCore.QRect(80, 540, 71, 71))
  self.b_0.setObjectName("b_0")
  self.b_pt = QtWidgets.QPushButton(self.centralwidget)
  self.b_pt.setGeometry(QtCore.QRect(10, 540, 71, 71))
  self.b_pt.setObjectName("b_pt")
  self.b_del = QtWidgets.QPushButton(self.centralwidget)
  self.b_del.setGeometry(QtCore.QRect(220, 470, 71, 71))
  self.b_del.setObjectName("b_del")
  self.b_clc = QtWidgets.QPushButton(self.centralwidget)
  self.b_clc.setGeometry(QtCore.QRect(290, 470, 71, 71))
  self.b_clc.setObjectName("b_clc")
  MainWindow.setCentralWidget(self.centralwidget)
  self.menubar = QtWidgets.QMenuBar(MainWindow)
  self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 30))
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
  self.b_1.setText(_translate("MainWindow", "1"))
  self.b_2.setText(_translate("MainWindow", "2"))
  self.b_3.setText(_translate("MainWindow", "3"))
  self.b_6.setText(_translate("MainWindow", "6"))
  self.b_4.setText(_translate("MainWindow", "4"))
  self.b_5.setText(_translate("MainWindow", "5"))
  self.b_8.setText(_translate("MainWindow", "8"))
  self.b_9.setText(_translate("MainWindow", "9"))
  self.b_7.setText(_translate("MainWindow", "7"))
  self.b_eq.setText(_translate("MainWindow", "="))
  self.b_mod.setText(_translate("MainWindow", "%"))
  self.b_bra_l.setText(_translate("MainWindow", "("))
  self.b_div.setText(_translate("MainWindow", "/"))
  self.b_add.setText(_translate("MainWindow", "+"))
  self.b_sub.setText(_translate("MainWindow", "-"))
  self.b_mul.setText(_translate("MainWindow", "*"))
  self.b_pow.setText(_translate("MainWindow", "^"))
  self.b_pai.setText(_translate("MainWindow", "π"))
  self.b_bra_r.setText(_translate("MainWindow", ")"))
  self.b_0.setText(_translate("MainWindow", "0"))
  self.b_pt.setText(_translate("MainWindow", "."))
  self.b_del.setText(_translate("MainWindow", "删除"))
  self.b_clc.setText(_translate("MainWindow", "清空"))





"逻辑部分"





'''
pluginsPath='PyQt5/Qt/plugins'
if os.path.exists(pluginsPath):#指定插件路径。源码运行时不会生效，打包后运行检测到路径，加载插件
 QApplication.addLibraryPath(pluginsPath)
'''
class MyMainWindow(QMainWindow, Ui_MainWindow):

 def forge_link(self):
  self.b_0.clicked.connect(self.button_event(0))
  self.b_1.clicked.connect(self.button_event(1))
  self.b_2.clicked.connect(self.button_event(2))
  self.b_3.clicked.connect(self.button_event(3))
  self.b_4.clicked.connect(self.button_event(4))
  self.b_5.clicked.connect(self.button_event(5))
  self.b_6.clicked.connect(self.button_event(6))
  self.b_7.clicked.connect(self.button_event(7))
  self.b_8.clicked.connect(self.button_event(8))
  self.b_9.clicked.connect(self.button_event(9))
  self.b_add.clicked.connect(self.button_event('+'))
  self.b_sub.clicked.connect(self.button_event('-'))
  self.b_mul.clicked.connect(self.button_event('*'))
  self.b_div.clicked.connect(self.button_event('/'))
  self.b_pow.clicked.connect(self.button_event('**'))
  self.b_bra_l.clicked.connect(self.button_event('('))
  self.b_bra_r.clicked.connect(self.button_event(')'))
  self.b_mod.clicked.connect(self.button_event('%'))
  self.b_pai.clicked.connect(self.button_event('3.1415926'))
  self.b_pt.clicked.connect(self.button_event('.'))
  self.b_del.clicked.connect(self.delete_event)
  self.b_clc.clicked.connect(self.clear_event)
  self.b_eq.clicked.connect(self.calc_complish)

 def __init__(self, parent=None):
  super(MyMainWindow, self).__init__(parent)
  self.setupUi(self)
  self.forge_link() #连接槽函数

 def button_event(self,arg):
  # print(dir(self.e_view))
  global e_view
  e_view=self.e_view
  def fun():  #返回一个自定义的槽函数
   global e_view
   txt = e_view.toPlainText()
   e_view.setText(txt + str(arg))
  return fun

 def calc_complish(self):
  txt=self.e_view.toPlainText()
  ans=''
  try:
   ans=str(eval(txt))
  except BaseException:
   ans='MathError'
  # print(ans)
  self.clear_event()
  self.e_view.setText(ans)
  self.l_hist.addItem(txt+'='+ans)

 def clear_event(self):
  self.e_view.setText('')

 def delete_event(self):
  txt = self.e_view.toPlainText()
  txt=txt[:len(txt)-1]
  self.e_view.setText(txt)

if __name__ == '__main__':
 app=QApplication(sys.argv)
 myWin=MyMainWindow()
 myWin.show()
 sys.exit(app.exec())