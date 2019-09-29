from findARoot import findARoot
            
value = int(input("Enter a number: "))
answer = findARoot(value)
if (answer == []):
    print("No root found")
else:
    print(str(answer[0]) + '^' + str(answer[1]) + ' = ' + str(value) )