# 가위/바위/보를 선택하세요 가위 Enter
# 나:가위
# 컴:바위
# 결과:짐
import random

mine = input("가위/바위/보를 선택하세요")
com = ""
result = ""

rnd = random.random() * 2 + 1
if rnd >= 1:
    com = "가위"
elif rnd >= 2:
    com = "바위"
else:
    com = "보"

if com == mine:
    result = "비김"
elif com == "바위" and mine == "가위" or com == "가위" and mine == "보" or com == "보" and mine == "주먹":
    result = "짐"
else:
    result = "이김"

print("mine:",mine)
print("com:",com)
print("result:",result)
