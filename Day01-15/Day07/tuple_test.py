import sys
"""
使用元组: 与列表类似，也是一种容器数据类型，可以用一个变量（对象）来存数多个数据

不同点：元组的数据不能被修改
"""

# 定义元组
t = ('今天', 7, True, 14.40)
print(t)
# 获取元组中的元素
print(t[0])  # 今天
print(t[3])  # 14.4
# 遍历元组中的值
for member in t:
    print(member, end=',')  # 今天,7,True,14.4
print()
# 重新给元组赋值
# t[0] = '罗云熙'  # TypeError: 'tuple' object does not support item assignment
# 变量t重新引用了新的元组，原来的元组将被垃圾回收
t = ('罗云熙', 7, True, 14.40)
print(t)  # ('罗云熙', 7, True, 14.4)
# 将元组转换成列表
person = list(t)
print(person)  # ['罗云熙', 7, True, 14.4]
# 列表是可以修改他的元素的
person[3] = '31.0'
print('列表大小：', sys.getsizeof(person))
print(person)  # ['罗云熙', 7, True, '31.0']
# 将列表转换成元组
tuple_new = tuple(person)
print('元组大小：', sys.getsizeof(tuple_new))
print(tuple_new)  # ('罗云熙', 7, True, '31.0')

"""
思考： 为什么有了列表，还需要元组

1.元组中的元素无法修改：
    如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，（多线程）
    当然如果一个方法要返回多个值，使用元组也是不错的选择。
2.元组在创建时间和占用的空间上优于列表
"""