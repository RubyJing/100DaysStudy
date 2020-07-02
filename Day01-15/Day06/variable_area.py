"""
变量的作用域
"""


def foo():
    # 嵌套作用域
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        # 局部作用域
        c = True
        print(a)
        print(b)
        print(c)

    bar()


def foo2():
    global a
    a = 200
    print(a)


if __name__ == '__main__':
    # a是全局变量
    a = 100
    foo()
    foo2()
