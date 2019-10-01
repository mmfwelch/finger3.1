from math import copysign

def findARoot(value):
    if (value == 0):
        return [0,2]

    root = copysign(1, value)
    increment = copysign(1, value)

    while True:
        power = 2
        if abs(root)**power > abs(value):
            return []
        while power < 6:
            guess = root**power
            if guess == value:
                return [root, power]
            power = power + 1
        root = root + increment
    return []

