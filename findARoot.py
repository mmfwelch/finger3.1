
def findARoot(value):
    if (value == 0):
        return [0,2]
    answer = []
    searchComplete = False
    if (value > 0):
        root = 2
        increment = 1
    else:
        root = -2
        increment = -1
    guess = 0
    while not searchComplete:
        power = 2
        if abs(root)**power > abs(value):
            searchComplete = True
            break
        while power < 6 and not searchComplete:
            guess = root**power
            if guess == value:
                # Could just return [root, power]
                answer = [root, power]
                searchComplete = True
                break
            elif abs(guess) > abs(value):
                break
            power = power + 1
        root = root + increment
    return answer

