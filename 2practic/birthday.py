import random
def birthday_probability(people):
    p = 1.0
    for i in range(people):
        p = p * (365 - i) / 365
    return 1 - p

def simulate_birthday(people, trials):
    count = 0
    for _ in range(trials):
        days = []
        for _ in range(people):
            days.append(random.randint(1, 365))
        if len(days) != len(set(days)):
            count = count + 1
    return count / trials


if __name__ == '__main__':
    print(birthday_probability(1))
    print(birthday_probability(23))
    print(birthday_probability(50))
    print(birthday_probability(366))
    print(' ')

    print(simulate_birthday(23, 100000))
