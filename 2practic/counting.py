def factorial(n):
    if n<0:
        return None
    elif n == 0:
        return 1
    k=1
    for g in range(1, n+1):
       k=k*g
    return k


def arrangements(n, k):
    if k>n:
        return 0
    n_fac = factorial(n)
    k2=factorial(n-k)
    return n_fac // k2

def combinations(n, k):
    return arrangements(n,k) // factorial(k)

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(5))
    print(factorial(-1))
    print(' ')

    print(arrangements(13, 6))
    print(arrangements(4, 2))
    print(arrangements(5, 5))
    print(arrangements(3, 5))
    print(' ')

    print(combinations(13, 6))
    print(combinations(4, 2))
    print(combinations(64, 8))
    print(combinations(5, 0))