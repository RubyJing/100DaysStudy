"""
寻找水仙花数
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""
print('在100~1000之间存在的水仙花数为下：')
for i in range(100, 1000):
    a = i // 100  # 百位
    b = i // 10 % 10  # 十位
    c = i % 10  # 个位
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)

"""
正整数反转
"""
num = int(input("请输入一个正整数："))
if num > 0:
    reverse_num = 0
    while num > 0:
        reverse_num = reverse_num * 10 + num % 10
        num //= 10
    print(reverse_num)
else:
    print('不是正整数')

"""
百钱百鸡问题
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for x in range(1, 20):
    for y in range(1, 33):
        if x * 5 + 3 * y + (100 - x - y) / 3 == 100:
            print("用100块钱买一百只鸡,公鸡%d只，母鸡%d只，小鸡%d只" % (x, y, 100 - x - y))

"""
生成斐波那契数列的前20个数
说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
"""
firstNum = 1
twoNum = 1
time = 0
while time < 20:
    mid = twoNum
    twoNum += firstNum
    firstNum = mid
    time += 1
    print(twoNum, ' ', end='')

"""
找出10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的约数）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
"""
for i in range(1, 10000):
    sum_num = 0
    for j in range(1, i):
        if i % j == 0:
            sum_num += j
    if sum_num == i:
        print(sum_num)

"""
输出100以内所有的素数
素数指的是只能被1和自身整除的正整数（不包括1）
"""
for i in range(1, 100):
    is_ok = True
    for j in range(1, i):
        if i % j == 0 and j != 1:
            is_ok = False
            break
    if is_ok:
        print(i, end=' ')
