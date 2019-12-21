
def GenerateCombination(N, ObjectNumber):
    # initiate the object B and C positions
    # Get all permutations of length 2
    combinlist = []
    for i in range(N):
        if i < N-1:
            j = i + 1
        else:
            j = 0
        combin = [ObjectNumber, i, j]
        combinlist.append(combin)
    return combinlist
