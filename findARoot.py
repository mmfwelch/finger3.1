
def findARoot(value):
    if (value == 0):
        return [0,2]
    answer = []
    if (value > 0):
        root = 2
        increment = 1
    else:
        root = -2
        increment = -1
    guess = 0
    while not answer:
        power = 2
        if abs(root)**power > abs(value):
            break
        while power < 6:
            guess = root**power
            if guess == value:
                answer = [root, power]
                break
            elif abs(guess) > abs(value):
                break
            power = power + 1
        root = root + increment
    return answer

