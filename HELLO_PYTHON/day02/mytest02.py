# 1~9까지의 수 중에서 3가지를 랜덤 중복없이 출력하시오
import random

arr9 = [1,2,3,4,5,6,7,8,9]

for i in range(100):
    rnd = int(random.random() * 9)
    a = arr9[rnd]
    b = arr9[0]
    arr9[0] = a
    arr9[rnd] = b

print("sem1 :",arr9[0],arr9[1],arr9[2])
#------------------------------------------------------------
print("배열 자르는 법 :", arr9[0:3])
#------------------------------------------------------------
import random

while True:

    ran1 = int(random.random() * 9 + 1)
    ran2 = int(random.random() * 9 + 1)
    ran3 = int(random.random() * 9 + 1)

    if ran1 != ran2 and ran1 != ran3 and ran2 != ran3: break

print("me :",ran1,ran2,ran3)
