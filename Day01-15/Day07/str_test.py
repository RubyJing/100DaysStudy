s1 = 'hello,world!'
s2 = "hello,world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello,
world!
"""
s4 = '''
hello,
world!
'''
print(s1, s2, s3, s4, end='')

'''
转义符 \
'''
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u5468\u9756'
print(s1, s2)

# 用字母r来表示转义符失效
s1 = r'\'hello,world!\''
s2 = r'\n\\hello,world!\\\n'
print(s1, s2)

"""
运算符
"""
s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print('ll' in s1)  # True
print('good' in s1)  # False

str2 = 'abc123456'
# 从字符串中取出指定的位置的字符（下标运算）
print(str2[2])  # c
# 字符串切片（从指定的开始索引到指定的结束索引）
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45

"""
其他特殊处理
"""
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获取字符串 首字母 大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获取字符串 每个单词 首字符 大写的拷贝
print(str1.title())  # Hello, World!
# 获取字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('o, w'))  # 4
print(str1.find('shit'))  # -1
# 与find类似，但找不到子串时会引发异常
print(str1.index('or'))  # 8
# print(str1.index('shit'))  # ValueError: substring not found
# 检测字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检测字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居住并在左侧填充指定的字符
print(str1.center(50, '*'))  # ******************hello, world!*******************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, '='))  # =====================================hello, world!
# 将字符串以指定的宽度靠左放置左侧填充指定的字符
print(str1.ljust(50, '='))  # =====================================hello, world!

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否由字母构成
print(str2.isalpha())  # False
# 检查字符串是否已数字和字母构成
print(str2.isalnum())  # True

str3 = ' 1234  56@qq.com  '
# 获得字符串去除左右两侧的空格的拷贝;也可以去除指定字符
print(str3.strip())
print(str3.lstrip())
str4 = '####123  56@qq.com'
print(str4.lstrip('#'))
print(str3.replace(' ', ''))

"""
格式化字符串
"""
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')  # 语法糖。在前加字母f

