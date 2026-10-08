import sys
sys.set_int_max_str_digits(100000)

def tetration(x, n):
    if n == 0:
        return 1

    return x ** tetration(x, n - 1)


if __name__ == "__main__":
    print(tetration(2, 0))  # 1
    print(tetration(2, 1))  # 2
    print(tetration(2, 2))  # 4
    print(tetration(2, 3))  # 16
    print(tetration(2, 4))  # 65536
    print(tetration(3, 2))  # 27
    print(tetration(5, 2))  # 3125