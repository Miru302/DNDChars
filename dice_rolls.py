from random import randint


def roll20():
    return randint(1, 20)


def roll10():
    return randint(1, 10)


def roll8():
    return randint(1, 8)


def roll6():
    return randint(1, 6)


def roll(a, b):
    result = 0
    for i in range(a):
        pass
        result = result + randint(1, b)
    return result


# testing
print roll(1, 6)
