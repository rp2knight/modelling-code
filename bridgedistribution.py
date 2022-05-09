import random

deck = []

for i in range(2, 15):
    deck.append([i, 'c'])
    deck.append([i, 'd'])
    deck.append([i, 'h'])
    deck.append([i, 's'])

def point(card):
    if (card[0] > 9):
        return(card[0]-10)
    return(0)

def value(hand, pos=0):
    val = 0
    for i in range(13*pos, 13*pos+13):
        val += point(hand[i])
    return(val)

def suitcount(hand, suit, pos=0):
    val = 0
    for i in range(13*pos, 13*pos+13):
        if (hand[i][1] == suit):
            val += 1
    return(val)

def shape(hand, pos=0):
    shape = []
    shape.append(suitcount(hand, 's', pos))
    shape.append(suitcount(hand, 'h', pos))
    shape.append(suitcount(hand, 'd', pos))
    shape.append(suitcount(hand, 'c', pos))
    return(shape)

def sortshape(hand, pos=0):
    return(sorted(shape(hand, pos), reverse=True))

def isbalanced(hand, pos=0):
    s = sortshape(hand, pos)
    if ((s == [4, 3, 3, 2]) or (s == [4, 4, 3, 2]) or (s == [5, 3, 3, 2])):
        return(True)
    s = shape(hand, pos)
    if ((s == [4, 2, 5, 2]) or (s == [2, 4, 5, 2]) or (s == [4, 2, 2, 5]) or (s == [2, 4, 2, 5])):
        return(True)
    return(False)

def opens1d(hand):
    if ((value(hand) > 16) or (value(hand) < 11)):
        return(False)
    if ((value(hand) == 16) and not isbalanced(hand)):
        return(False)
    if ((value(hand) > 10) and (value(hand) < 14) and isbalanced(hand)):
        return(False)
    if ((value(hand) == 11) and isbalanced(hand)):
        return(False)
    if ((suitcount(hand, 's') > 4) or (suitcount(hand, 'h') > 4) or (suitcount(hand, 'c') > 5) or (suitcount(hand, 'd') < 2)):
        return(False)
    return(True)

random.shuffle(deck)

samples = 1000000
good = 0
bad = 0
neutral = 0


while(i < samples):
    random.shuffle(deck)
    if ((value(deck) < 16) and (value(deck) > 10) and (suitcount(deck, 's') == 6) and (suitcount(deck, 'h') == 4)):
        if ((value(deck, 2) > 5) and (value(deck, 2) < 13) and (suitcount(deck, 's', 2) < 3) and (suitcount(deck, 'd', 2) < 7) and (suitcount(deck, 'c', 2) < 7)):
            if ((suitcount(deck, 'h', 2) - suitcount(deck, 's', 2) < 1) or ((suitcount(deck, 'h', 2) == 2) and (suitcount(deck, 's', 2) == 0))):
                neutral += 1
            if ((suitcount(deck, 'h', 2) == suitcount(deck, 's', 2)+1) or ((suitcount(deck, 'h', 2) == 3) and (suitcount(deck, 's', 2) == 1))):
                good += 1
            if ((suitcount(deck, 'h', 2) - suitcount(deck, 's', 2) > 1) and (suitcount(deck, 'h', 2) > 2) and not ((suitcount(deck, 'h', 2) == 3) and (suitcount(deck, 's', 2) == 1))):
                bad += 1
            i += 1
    if (i%1000 == 0):
        print(i, good, bad, neutral)


print(samples, good, bad, neutral)
        

