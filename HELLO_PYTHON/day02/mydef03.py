import random

def myrandom():
    ran = 0
    
    if random.random() > 0.5:
        ran = 1
    else:
        ran = 0    
        
    return ran    
    
rnd = myrandom()
print("rnd",rnd)    