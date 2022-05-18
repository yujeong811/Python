import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.Qt import QPushButton, QSize
from conda.common._logic import TRUE

form_class = uic.loadUiType("myomok02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flag_wb = True
        self.flag_over = False
        self.pb2d = []
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                obj = QPushButton(self)
                obj.setText('')
                obj.setIcon(QtGui.QIcon('0.png'))
                obj.setIconSize(QSize(40, 40))
                obj.setGeometry(0 + 40*j, 0 + 40*i, 40, 40)
                obj.clicked.connect(self.myclick)
                obj.setToolTip("{},{}".format(i, j))
                line.append(obj)
            self.pb2d.append(line) #배열에 배열을 넣어 2차원 배열 생성
        
        self.myrender()
        self.pb.clicked.connect(self.myreset)
        self.show()
    
    def myreset(self):
        self.flag_wb = True
        self.flag_over = False
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
        self.myrender()        
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))   
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
                
    def myclick(self):
        if self.flag_over :
            return
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(',')
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        
        up = self.checkUP(i, j, stone)
        dw = self.checkDW(i, j, stone)
        ri = self.checkRI(i, j, stone)
        le = self.checkLE(i, j, stone)
        ur = self.checkUR(i, j, stone)
        ul = self.checkUL(i, j, stone)
        dr = self.checkDR(i, j, stone)
        dl = self.checkDL(i, j, stone)
        # print(up, dw, ri, le, ur, ul, dr, dl)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = ri + le + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flag_over = True
            if self.flag_wb : 
                QMessageBox.about(self, 'omok', '백돌승리')
            else:
                QMessageBox.about(self, 'omok', '흑돌승리')
                
        self.flag_wb = not self.flag_wb
    
    def checkDL(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDR(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUL(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkUR(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkLE(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkRI(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDW(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkUP(self, i ,j , stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt                
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                      
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()