import time

# def main():
#     f = None
#     try:
#         f = open('测试文本.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#     finally:
#         if f:
#             f.close()


"""
如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，
"""
# def main():
#     try:
#         with open('测试文本.txt', 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')

"""
使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
"""


def main():
    try:
        # 一次性读取整个文件内容
        with open('介绍.txt', 'r', encoding='utf-8') as f:
            print(f.read())

        # 通过for-in循环逐行读取
        with open('介绍.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
        print()

        # 读取文件按行读取到列表中
        with open('介绍.txt', encoding='utf-8') as f:
            lines = f.readline()
        print(lines)
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')


if __name__ == '__main__':
    main()