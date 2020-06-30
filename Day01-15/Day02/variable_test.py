"""
使用变量保存数据并进行加减乘除运算

"""
h = 321
g = 12
print(h + g)
print(h - g)
print(h * g)
print(h / g)

# 变量类型
a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 运算符
z = int(input('请输出一个数字：'))
x = int(input('请输出一个数字：'))
print('%d + %d = %d' % (z, x, z + x))
print('%d - %d = %d' % (z, x, z - x))
print('%d * %d = %d' % (z, x, z * x))
print('%d / %d = %d' % (z, x, z / x))
print('%d // %d = %d' % (z, x, z // x))
print('%d %% %d = %d' % (z, x, z % x))
print('%d ** %d = %d' % (z, x, z ** x))

v = 10
n = 3
v += n  # 相当于：v = v + n
v *= v + 2  # 相当于：v = v * (v + 2)
print(v)

# 比较运算符和逻辑运算符的使用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 = ', flag0)
print('flag1 = ', flag1)
print('flag2 = ', flag2)
print('flag3 = ', flag3)
print('flag4 = ', flag4)
print('flag5 = ', flag5)

