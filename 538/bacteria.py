import random
import math
import queue
import matplotlib.pyplot as plt
import numpy

def simulate(p):
    q = queue.SimpleQueue()
    q.put(0)
    q.put(1)
    count = -3
    prev = 1
    current = 1

    while not ((prev == 0) and (current == 0)):
        prev = current
        current = q.get()
        if current == 0:
            count += 1
            q.put(0)
        if current == 1:
            if random.random() < p:
                q.put(1)
                q.put(1)
##        print(prev, current)

    return count

results = []
graph = []
xaxis = []

simulations = 100000
high = 500
offset = 4

for i in range(2, high+1):
    p = (i-2)/(2*i)
    total = 0
    for j in range(simulations):
        total += simulate(p)
    results.append(total/simulations)
    xaxis.append(math.log(i+offset))
#    graph.append(math.log(.2736*i))
    print(i)

a = numpy.polyfit(xaxis, results, 1)
a1 = a[0]
a0 = a[1]
for i in range(2, high+1):
    graph.append(a1*math.log(i+1)+a0)

plt.plot(range(2, high+1), results, 'b-')
plt.plot(range(2, high+1), graph, 'r-')
plt.show()

print(a1, a0)
