
def maxStolenValue(Amount):
    Length = len(Amount)
    if Length == 0:
        return 0
    if Length == 1:
        return Amount[0]
    Dynamic = [0] * Length
    Dynamic[0] = Amount[0]
    Dynamic[1] = max(Amount[0], Amount[1])
    for i in range(2, Length):
        Dynamic[i] = max(Dynamic[i-1], Amount[i] + Dynamic[i-2])
    return Dynamic[-1]
Amount = [6, 7, 1, 3, 8, 2, 5]
print(maxStolenValue(Amount))   















for i in range(5):
    for j in range(5):
        if (i % 2 == 0 and j == 4):
            print(i+2, end="")
        elif (i % 2 == 1 and j == 0):
            print(i+2, end="")
        else:
            print(i+1, end="")
    print()



    
def isDisarium(num):
    temp = num
    result = 0
    length = len(str(num))
    
    for i in range(length):
        digit = int(str(num)[i])
        result += digit ** (i + 1)
    
    return result == num


def firstNDisarium(number):
    count = 0
    num = 0
    print(f"First {number} Disarium numbers are:")
    while count < number:
        if isDisarium(num):
            print(num, end=" ")
            count += 1
        num += 1
    print("\n")


def disariumInRange(start, end):
    print(f"Disarium numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if isDisarium(num):
            print(num, end=" ")
    print()


firstNDisarium(5)

disariumInRange(1, 200)





def isDisarium(num):
    temp = num
    result = 0
    length = len(str(num))
    
    for i in range(length):
        digit = int(str(num)[i])
        result += digit ** (i + 1)
    
    return result == num


def firstNDisarium(number):
    count = 0
    num = 0
    print(f"First {number} Disarium numbers are:")
    while count < number:
        if isDisarium(num):
            print(num, end=" ")
            count += 1
        num += 1
    print("\n")

# Function to print Disarium numbers in a range
def disariumInRange(start, end):
    print(f"Disarium numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if isDisarium(num):
            print(num, end=" ")
    print()

# Example usage
firstNDisarium(5)
disariumInRange(1, 200)
