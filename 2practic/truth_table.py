from itertools import product

def truth_table(n: int):
    return list(product([0, 1], repeat=n))
if __name__ == '__main__':
    print(truth_table(1))
    print(truth_table(2))
    print(truth_table(3))
    print(truth_table(0))