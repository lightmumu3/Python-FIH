# -*- coding: utf-8 -*-
import sys
from MainEvent import *
import sip

if __name__=="__main__":
    
    app = QApplication(sys.argv)
    ms = MainWindow()
    ms.show()
    sys.exit(app.exec_())

    







