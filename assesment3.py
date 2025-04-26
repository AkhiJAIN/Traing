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
