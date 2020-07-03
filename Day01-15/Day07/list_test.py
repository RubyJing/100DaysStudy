import sys

"""
列表（list）:值的有序序列，每个值都可以通过索引进行标识
"""

"""
定义列表，遍历列表以及列表下标运算
"""

list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]
# 乘号标识列表元素的重复
list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']
# 计算列表长度（元素个数）
print(len(list1))  # 5
# 下标（索引）运算
print(list1[0])  # 1
print(list1[4])  # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同事获取元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

"""
向列表中添加元素以及如何从列表中移除元素
"""
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)  # 往列表后加入
list1.insert(1, 400)  # 往列表前加入
print(list1)  # [1, 400, 3, 5, 7, 100, 200]
# 合并两个列表
list1.extend([1000, 2000])
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
list1 += [1100, 2100]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000, 1100, 2100]
print(len(list1))  # 11
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000, 1100, 2100]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000, 2000, 1100]
# 清空列表元素
list1.clear()
print(list1)  # []

"""
列表切片操作
通过切片操作我们可以实现对列表的复制
或者将列表中的一部分取出来创建出新的列表
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # ['apple', 'strawberry', 'waxberry']
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
# fruits3 = fruits
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)  # ['pitaya', 'pear']
# 可以通过反向切片操作来获取倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

"""
列表排序操作
"""
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝，不会修改传入的列表
list3 = sorted(list1, reverse=True)
# 通过Key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

"""
生成式：可以使用列表的生成式语法来创建列表
"""
f = [x for x in range(1, 10)]
print(f)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后，元素以及准备就绪，所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 10)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数：192
print(f)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 请注意下面的代码创建的不是一个列表，而是一个生成器对象
# 通过生成器可以获取到数据，但它不占用额外的空间存储数据
# 每次需要数据的时候，就通过内部的运算得到数据（需要花费额外的时间）
f = (x ** 2 for x in range(1, 10))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存数数据的空间：120 （时间换空间）
print(f)
for val in f:
    print(val, end=',')

"""
定义生成器：通过yield 关键字将一个普通函数改造成生成器函数
"""
'''
生成斐波拉切数列的生成器(第三项，等于前两项之和）
Fo = 0
F1 = 1
Fn = F n-1 + F n-2 (n >= 2)
'''


def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


def main():
    for i in fib(20):
        print(i, end=',')


if __name__ == '__main__':
    print()
    main()
