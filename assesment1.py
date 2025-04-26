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
