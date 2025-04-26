'''There are n houses build in a line, each of which contains some value in it.

A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will
tell his two neighbors left and right side.

What is the maximum stolen value?

Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}

Sample Output: 20'''

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

'''output=20'''
'''Print the pattern
11112
32222
33334
54444
55556'''


for i in range(5):
    for j in range(5):
        if (i % 2 == 0 and j == 4):
            print(i+2, end="")
        elif (i % 2 == 1 and j == 0):
            print(i+2, end="")
        else:
            print(i+1, end="")
    print()

'''output:11112
32222
33334
54444
55556'''


''' Write program to find first n Disarium numbers and Disarium numbers between two given numbers.

A number is said to be Disarium if it is equal to sum of its digits raised to the power of their respective position in the number. 
For example, 135 is a Disarium number. Because, it is equal to sum of its digits raised to the power of their respective position.

135 = 1^1 + 3^2 + 5^3
135 = 1 + 9 + 125
'''

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


'''outputFirst 5 Disarium numbers are:
0 1 2 3 4

Disarium numbers between 1 and 200 are:
1 2 3 4 5 6 7 8 9 89 135 175'''
