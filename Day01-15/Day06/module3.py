def foo():
    pass


def bar():
    pass


# _name_是Python中一个隐含的变量，它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是_main
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
