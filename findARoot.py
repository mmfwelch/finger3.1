
def findARoot(value):
    if (value == 0):
        return [0,2]
    solutionFound = False
    searchComplete = False
    if (value > 0):
        root = 2
        increment = 1
    else:
        root = -2
        increment = -1
    guess = 0
    while searchComplete != True:
        power = 2
        if abs(root)**power > abs(value):
            searchComplete = True
            break
        while power < 6 and searchComplete != True:
            guess = root**power
            if guess == value:
                # Could just return [root, power]
                searchComplete = True
                solutionFound = True
                break
            elif abs(guess) > abs(value):
                break
            power = power + 1
        if searchComplete != True:
            root = root + increment
    if solutionFound:
        return [root, power]
    else:
        return []

