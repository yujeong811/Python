import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("myqt09.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick) 
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
    
    def myclick(self):
        me = self.le_mine.text()
                      
        rnd = int(random.random() * 3) + 1
        
        if rnd == 1:
            self.le_com.setText("가위")
        elif rnd == 2:
            self.le_com.setText("바위")
        else :
            self.le_com.setText("보")

        if me == self.le_com.text():
            self.le_result.setText("비겼습니다.")
        elif me == "가위" and self.le_com.text() == "바위" or  me == "바위" and self.le_com.text() == "보" or  me == "보" and self.le_com.text() == "가위" :
            self.le_result.setText("졌습니다.")
        else : 
            self.le_result.setText("이겼습니다.")
          
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()