
def findARoot(value):
    if (value == 0):
        return [0,2]
    if (value > 0):
        root = 2
        increment = 1
    else:
        root = -2
        increment = -1
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

