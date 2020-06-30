"""
英制单位英寸和公制单位厘米互换
"""
unit = str(input("请输入单位（英寸in/厘米cm）："))
length = float(input("请输入长度："))
if unit == '英寸' or unit == 'in':
    result = length * 2.54
    resultUnit = '厘米'
elif unit == '厘米' or unit == 'cm':
    result = length / 2.54
    resultUnit = '英寸'
else:
    result = 0
    resultUnit = '没有对应的类型'
print('%.2f %s' % (result, resultUnit))

"""
百分制成绩转换为等级制成绩
要求：
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
"""
score = int(input("请输入成绩："))
if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'E'
print('最终成绩为：', result)

"""
输入三条边长，如果能构成三角形就计算周长和面积
面积：海伦公式
"""
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a + b > c and b + c > a and a + c > b:
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("周长是%.2f,面积是%.2f" % (perimeter, area))
else:
    print("不能组成一个三角形")
