"""
实现计算求最大公约数和最小公倍数的函数
"""


def gcd(num1, num12):
    """求最大公约数"""
    if num1 > num12:
        num1, num12 = num12, num1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num12 % i == 0:
            return i


def lcm(num1, num12):
    """最小公倍数"""
    return num1 * num12 // gcd(num1, num12)


"""
实现判断一个数是不是回文数的函数
"""


def palindrome(num):
    if num < 10:
        return False
    return num == reverse(num)


def reverse(num):
    """反转数字"""
    reverse_num = 0
    while num > 0:
        last_num = num % 10
        reverse_num = reverse_num * 10 + last_num
        num //= 10
    return reverse_num


"""
实现判断一个数是不是素数的函数
"""


def prime_number(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


"""
判断一个数是不是回文素数的函数
"""


def palindrome_prime_number(num):
    return palindrome(num) and prime_number(num)


if __name__ == '__main__':
    # x = int(input("x="))
    # y = int(input("y="))
    # max_num = gcd(x, y)
    # min_num = lcm(x, y)
    # print("最大公约数为：%d,最小公倍数：%d" % (max_num, min_num))

    # z = int(input("z="))
    # print("%d是否回文数：" % z, palindrome(z))

    # z = int(input("z="))
    # print("%d是否素数：" % z, prime_number(z))

    z = int(input("z="))
    print("%d是否回文素数：" % z, palindrome_prime_number(z))
