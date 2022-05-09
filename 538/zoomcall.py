import random
import math
import matplotlib.pyplot as plt

##This function does a simulation of a Zoom call
##with population people in it and returns the
##number of people that are in the Zoom call
##with everyone else.

def simulate(population):
    entrances = []
    exits = []
    witnesses = []
    firstexit = 1
    lastentrance = 0

    for i in range(population):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (y < x):
            z = y
            y = x
            x = z
        entrances.append(x)
        exits.append(y)
        if (x > lastentrance):
            lastentrance = x
        if (y < firstexit):
            firstexit = y

    for i in range(population):
        if (entrances[i] < firstexit):
            if (exits[i] > lastentrance):
                witnesses.append(i)
    return(len(witnesses))

##These are some variables that are used for
##the simulation.  The code runs simulations
##times, and each simulation is with people
##number of people in the Zoom call.  successes
##is the number of Zoom calls with a person
##in the call with everyone else, and
##supersuccesses is the number of Zoom calls
##with at least two people in the call with
##everyone else.

simulations = 100000
people = 10000
successes = 0
supersuccesses = 0
maximum = 0
results = []

for i in range(simulations):
    z = simulate(people)
    results.append(z)
    if (i % 100 == 0):
        print(i)
    if (z > 0):
        successes += 1
    if (z > 1):
        supersuccesses += 1
    if (z > maximum):
        maximum = z

displayset = []

for k in range(maximum+1):
    results.append(k)
    displayset.append((results.count(k)-1)/simulations)

plt.plot(range(maximum+1), displayset, 'b-')
plt.show()

print(successes)
print(successes/simulations)
print(supersuccesses/simulations)
