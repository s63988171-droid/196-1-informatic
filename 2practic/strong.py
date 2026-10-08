def is_strong(n):
    original = n
    total = 0
    for digit in str(n):
        fact = 1
        for i in range(1, int(digit) + 1):
            fact *= i
        total += fact
    return total == original