import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("myqt07.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick) 
        self.show()
    
    def myclick(self):
        a = self.le_first.text()
        b = self.le_last.text()
        
        first = int(a)
        last = int(b)
        
        star = ""       
        for i in range(first,last+1):
            star += self.drawStar(i)

        self.te.setText(star)
        
    def drawStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret 
          
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()