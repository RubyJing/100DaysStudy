"""
 test1:将华氏温度转换为摄氏温度
    .1f表示小数点后保留1位有效数字
"""
f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')


"""
输入半径计算圆的周长和面积
"""
radius = float(input("请输入圆的半径："))
perimeter = 2 * 3.141592654 * radius
area = 3.141592654 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)


"""
输入年份 如果是闰年输出True 否则输出False
"""
year = int(input("请输入年份："))
is_leap = year % 4 == 0 \
          and year % 100 != 0 \
          or year % 400 == 0
print(is_leap)
