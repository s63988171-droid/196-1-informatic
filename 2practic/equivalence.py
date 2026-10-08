def are_equivalent(f, g, n):
    for i in range(2 ** n):
        args = []
        for j in range(n):
            args.append((i >> (n - 1 - j)) & 1)
        if f(*args) != g(*args):
            return False
    return True

def impl(a, b):
    return (not a) or b

def f1(a, b):
    return not (a and b)

def g1(a, b):
    return (not a) or (not b)

if __name__ == "__main__":
    print(are_equivalent(f1, g1, 2))