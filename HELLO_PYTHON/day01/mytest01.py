# 앞수를 넣으세요 1 Enter
# 끝수를 넣으세요 10 Enter
# 당신의 수의 합은 55입니다

first = int(input("앞수를 넣으세요"))
last = int(input("끝수를 넣으세요"))
hap = 0

arr = list(range(first,last))

for i in arr:
    hap += i

print(hap)