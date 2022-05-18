import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myomok01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.com = ""
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick) 
        self.setCom()
        self.show()
    
    def myclick(self):        
        str_old = self.te.toPlainText()
        str_new = self.getBallStrike()
        self.te.setText(str_old + str_new)
        self.le.setText("")
        
    def setCom(self):
        arr9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        arr3 = []
        
        while len(arr3) < 3:
            rnd = (int)(random.random() * 9)
            if not(arr9[rnd] == "-1"):
                arr3.append(arr9[rnd])
                arr9[rnd] = "-1"
        
        self.com = arr3[0] + arr3[1] + arr3[2]
        print(self.com)
            
    def getBallStrike(self):
        ret = ""
        mytry = self.le.text()
        
        strike = 0
        ball = 0
        
        m1 = mytry[0:1]
        m2 = mytry[1:2]
        m3 = mytry[2:3]
        
        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        if m1 == c1:
            strike += 1        
        if m2 == c2:
            strike += 1            
        if m3 == c3:
            strike += 1
        
        if (m1 == c2) or (m1 == c3):
            ball += 1
        if (m2 == c1) or (m2 == c3):
            ball += 1            
        if (m3 == c1) or (m3 == c2):
            ball += 1
        
        if strike == 3:
            QMessageBox.about(self, "baseball", "congratulation")
        
        ret = mytry + " - " + str(strike) + "S " + str(ball) + "B\n"   
        
        return ret  
   
              
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()