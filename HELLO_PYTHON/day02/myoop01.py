class Animal:
    def __init__(self):
        print("Animal:생성자")    
        self.age = 0
                
    def getOld(self):
        self.age += 1
    
    def __del__(self):
        print("Animal:소멸자")    
    
class Human(Animal):
    def __init__(self):
        print("Human:생성자")
        super().__init__()
        self.skill_lang = 0
    
    def momstouch(self,stroke):  
        self.skill_lang += stroke
        
    def __del__(self):
        print("Human:소멸자")       
        
if __name__ == '__main__':
    hum = Human()                  
    print("myoop01",hum.skill_lang)
    print("myoop01",hum.age)  
    hum.getOld()
    hum.momstouch(10000)
    print("myoop01",hum.skill_lang)
    print("myoop01",hum.age)
    
    