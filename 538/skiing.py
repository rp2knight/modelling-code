import random

people = 3
samples = 1000000
totvalid = 0
totwon = 0

for j in range(samples):

    split1 = []
    split2 = []
    
    for i in range(people):
        split1.append(random.normalvariate(0,1))
        split2.append(random.normalvariate(0,1))
##        print(split1[i], split2[i])
##
##    print()

    valid = True
    win = True

    for i in range(1, people):
        if(split1[0] < split1[i]):
            valid = False
            win = False
        if(split1[0] + split2[0] < split1[i] + split2[i]):
            win = False

    if(valid):
        totvalid += 1
    if(win):
        totwon += 1

print(totvalid, totwon, totwon/totvalid)
    
    
