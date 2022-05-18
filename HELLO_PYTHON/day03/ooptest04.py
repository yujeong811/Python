class LeeJY:
    def __init__(self):
        self.money = 10
    def shout(self,angry):
        self.money += angry
        
class KimJE:
    def __init__(self):
        self.cnt_nuclear = 10
    def aoji(self):    
        self.cnt_nuclear += 1
        
class LeeUC(LeeJY,KimJE):
    def __init__(self):
        LeeJY.__init__(self)
        KimJE.__init__(self)

ljy = LeeUC()
print(ljy.money)
print(ljy.cnt_nuclear)
ljy.shout(1)
ljy.aoji()   
print(ljy.money)
print(ljy.cnt_nuclear)