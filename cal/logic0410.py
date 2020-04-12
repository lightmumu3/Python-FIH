from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import QCoreApplication
from cal_UI0410 import *     #调用Ui中的mainwindow
#from calc_interface import Ui_MainWindow
import os,sys

global e_view
from PyQt5 import QtCore, QtGui, QtWidgets

class MyMainWindow(QMainWindow, Ui_MainWindow):

 def forge_link(self):                                    ###########################
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
  #self.b_pow.clicked.connect(self.button_event('**'))
  #self.b_bra_l.clicked.connect(self.button_event('('))
  #self.b_bra_r.clicked.connect(self.button_event(')'))
  self.b_baifenhao.clicked.connect(self.button_event('%'))
  #self.b_pai.clicked.connect(self.button_event('3.1415926'))
  self.b_pt.clicked.connect(self.button_event('.'))
  self.b_delete.clicked.connect(self.delete_event)
  self.b_clear.clicked.connect(self.clear_event)
  self.b_eq.clicked.connect(self.calc_complish)
  ##self.b_close.clicked.connect(self.quit)
  self.b_close.clicked.connect(QCoreApplication.quit)
 def __init__(self, parent=None):
  super(MyMainWindow, self).__init__(parent)
  self.setupUi(self)
  self.forge_link() #连接槽函数

 def button_event(self,arg):  #这是啥？?????????
  # print(dir(self.e_view))
  global e_view
  e_view=self.e_view
  def fun():  #返回一个自定义的槽函数
   global e_view
   txt = e_view.toPlainText()
   e_view.setText(txt + str(arg))
  return fun

 def calc_complish(self):     #数字计算逻辑！！！！！！！！！！！！！！！！！！！
  txt=self.e_view.toPlainText()
  ans=''
  try:
   ans=str(eval(txt))
  except BaseException:
   ans='MathError'
  # print(ans)
  self.clear_event()
  self.e_view.setText(ans)
  #self.l_hist.addItem(txt+'='+ans)

 def clear_event(self):
  self.e_view.setText('')    #清空窗口函数

 def delete_event(self):
  txt = self.e_view.toPlainText()       #定义变量txt为控件上所显示的纯文本
  txt=txt[:len(txt)-1]
  self.e_view.setText(txt)      #删除字符



