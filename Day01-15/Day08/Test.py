class Test:
    def __init__(self, foo):
        self._foo = foo

    # 以单下划线开头来表示属性是受保护
    def _bar(self):
        print(self._foo)
        print('_bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test._bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test._foo)


if __name__ == '__main__':
    main()
