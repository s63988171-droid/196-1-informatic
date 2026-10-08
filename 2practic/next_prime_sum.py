def min_to_prime(numbers):
    total_sum = sum(numbers)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(total_sum):
        return 0

    add = 1
    while True:
        if is_prime(total_sum + add):
            return add
        add += 1
if __name__ == '__main__':
    print(min_to_prime([3, 1, 2]))
    print(min_to_prime([2, 12, 8, 4, 6]))
    print(min_to_prime([5, 2]))