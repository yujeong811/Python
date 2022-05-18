# 1~45까지의 수 중에서 6가지를 랜덤 중복없이 출력하시오

import random

arr = list(range(1,46))
a = random.sample(arr, 6)
print("me :",a) 
#-----------------------------------------
arr45 = list(range(1,46))
arr6 = []

while True:
    rnd = int(random.random() * 45)
    if arr45[rnd] == -1:
        pass
    else:
        arr6.append(arr45[rnd])
        arr45[rnd] = -1
    if len(arr6) >= 6: break     

print("sem :",arr6)