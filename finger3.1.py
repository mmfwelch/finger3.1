from findARoot import findARoot
            
value = int(input("Enter a number: "))
answer = findARoot(value)
if (answer == []):
    print("No root found")
else:
    print(answer[0], '^', answer[1], ' = ', value, sep='')