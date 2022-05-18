# 첫수를 넣으세요 1 Enter
# 끝수를 넣으세요 5 Enter
# 배수를 넣으세요 2 Enter
# 1에서 5까지의 2의 배수의 합은 6입니다

first = int(input("첫 수를 넣으세요"))
last = int(input("끝 수를 넣으세요"))
mul = int(input("배수를 넣으세요"))
hap = 0

for i in range(first,last):
    if (i % mul == 0):
        hap += i

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(first,last,mul,hap))