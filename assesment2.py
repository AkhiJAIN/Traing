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