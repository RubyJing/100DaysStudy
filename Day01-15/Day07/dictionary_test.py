"""
使用字典:另一种可变容器模型
它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开
"""
# 创建字典的字面量语法
scores = {'罗云熙': 30, '张艺兴': 28, '张三': 40}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)

# 通过建可以获取字典中对应的值
print(scores['罗云熙'])
print(scores['张艺兴'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['程潇'] = 20
scores['范冰冰'] = 35
scores.update(赵四=45, 尼古拉=100)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值，但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('赵四', 50))
print(scores)
# 清空字典
scores.clear()
print(scores)
