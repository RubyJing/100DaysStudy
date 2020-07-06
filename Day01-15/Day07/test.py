import os
import time
import random

"""
练习1：在屏幕上显示跑马灯文字
"""


def marquee():
    content = '--LPL第一赛区,JKL第一ADC!--'
    while True:
        os.system('cls')  # 执行cls命令清空Python控制台
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
"""


def general_captcha(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度（默认4哥字符）
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_range = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, random_range)
        code += all_chars[index]
    return code


"""
练习3：设计一个函数返回给定文件名的后缀名
"""


def get_file_suffix_name(filename='', has_point=False):
    """
    获取文件后缀名
    :param filename: 文件命
    :param has_point: 返回的后缀名是否带点（默认否）
    :return: 文件后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_point else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    marquee()
    print(general_captcha(10))
    print(get_file_suffix_name('sss.txt', True))