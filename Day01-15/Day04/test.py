"""
练习1：输入一个正整数判断是不是素数
素数指的是只能被1和自身整数的大于1的整数
"""

num = int(input("请输入一个正整数："))
if num > 0:
    is_prime = True
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print("%d是素数" % num)
    else:
        print("%d不是素数" % num)
else:
    print("这不是正整数")

"""
练习2：输入两个正整数，计算它们的最大公倍数和最小公约数

"""
num_one = int(input("请输入一个正整数"))
num_two = int(input("请输入一个正整数"))
greatest_common_divisor = num_one * num_two
print("最大公约数是 %d" % greatest_common_divisor)
if num_one >= num_two:
    length = num_two
else:
    length = num_one
least_common_multiple = 0
for x in range(2, length + 1):
    if num_one % x == 0 and num_two % x == 0:
        least_common_multiple = x
        break
if least_common_multiple == 0:
    print("没有最小公倍数")
else:
    print("最小公倍数是 %d" % least_common_multiple)

"""
练习3：输入两个正整数计算它们的最大公约数和最小公倍数

"""
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

"""
打印三角形图案
"""
row = int(input("请输入行数"))
for i in range(row + 1):
    for _ in range(i):
        print("*", end='')
    print()
# for i in range(row + 1):
#     for _ in range(row - i):
#         print(" ", end='')
#     for _ in range(i):
#         print("*", end='')
#     print()
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end='')
        else:
            print("*", end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end='')
    for j in range(i * 2 + 1):
        print("*", end='')
    print()
