import random

def game(turns, effort):
    net = 0
    for i in range(turns):
        delta = 0
        if net == 0:
            if random.random() < .5:
                delta = 1
        if net > 0:
            if random.random() < .5 - effort:
                delta = 1
        if net < 0:
            if random.random() < .5 + effort:
                delta = 0
        net += delta
        delta = 0
        if net == 0:
            if random.random() < .5:
                delta = -1
        if net > 0:
            if random.random() < .5 + effort:
                delta = -1
        if net < 0:
            if random.random() < .5 - effort:
                delta = -1
        net += delta
    return(net)

def sim(games, turns, effort):
    wins = 0
    losses = 0
    ties = 0
    for j in range(games):
        score = game(turns, effort)
        if score > 0:
            wins += 1
        if score == 0:
            ties += 1
        if score < 0:
            losses += 1
    return([wins, losses, ties])

sims = 10000
acc = 500
length = 10

for i in range(acc+1):
    print(sim(sims, length, .5*i/acc), .5*i/acc)
