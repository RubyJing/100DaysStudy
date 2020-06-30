import random

"""
用for循环实现1~100求和
"""
sumNum = 0
for x in range(101):
    sumNum += x
print(sumNum)

"""
用for循环实现1~100之间的偶数求和
"""
sumNum = 0
for x in range(1, 100, 2):
    sumNum += x
print(sumNum)

"""
猜数字游戏
"""
print("猜数字游戏 \n产生一个随机数，范围在1-100之间")
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入整数：'))
    if number < answer:
        print("小了")
    elif number > answer:
        print("大了")
    else:
        print("恭喜，你猜对了!")
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print("笨蛋")

"""
输出乘法九九口诀表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print()
