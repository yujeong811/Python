import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("myqt04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick) 
        self.show()
    
    def myclick(self):
        rnd = (int)(random.random() * 2) + 1
        
        if rnd == 1:
            self.le_com.setText("홀")
        else:
            self.le_com.setText("짝")  
        
        if self.le_mine.text() == self.le_com.text():
            self.le_result.setText("이김")   
        else:
            self.le_result.setText("짐")    
          
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()