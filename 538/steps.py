import itertools

def isValid(l, m):
    t = len(l)
    for i in range(t):
        for j in range(m):
            if (l[0:i].count(j) < l[0:i].count(j+1)):
                return(False)
    return(True)

total = 0

for l in itertools.permutations([0,0,0,0,1,1,1,2,2,3]):
    if (isValid(l, 3)):
        total += 1

print(total/(24*6*2))
