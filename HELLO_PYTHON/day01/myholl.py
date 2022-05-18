import random

com = ""
mine = input("홀/짝을 입력하세요")
result = ""

rnd = random.random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if mine == com:
    result = "이겼습니다"
else:
    result = "졌습니다"

print("com",com)
print("mine",mine)
print("result",result)

