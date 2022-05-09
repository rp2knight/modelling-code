import math

##This code moves you c units towards them.

def move(you, them, c):
    dx = them[0]-you[0]
    dy = them[1]-you[1]
    d = math.sqrt(dx**2 + dy**2)
    x = you[0] + dx*c/d
    y = you[1] + dy*c/d
    return([x, y])

##This function tests to see if you catch them given
##that you move s times as fast as them.  It moves you
##and them in increments of inc, which defaults to .001.

def test(you, them, s, inc=.001):
    while ((them[0] < 100) and (you[0] <= them[0])):
        them[0] += inc
        you = move(you, them, s*inc)
    return(them[0] < 100)

##This does binary search to find the slowest possible speed
##that catches Jarrison.  Quick testing shows that you don't
##catch Jarrison if you move 1.25 times as fast as him, and
##that you do if you move 1.29 times as fast as him, so I used
##those as the start points for the binary search.  acc is how
##accurate I wanted the search to be.

g1 = 1.25
g2 = 1.29
acc = .00000001

while(g2-g1 > acc):
    you = [0, 50]
    them = [0, 0]
    g = (g1 + g2)/2
    b = test(you, them, g)
    if b:
        g2 = g
    if not b:
        g1 = g

print(g1, g2)

##This code is to make a pretty picture.

import matplotlib.pyplot as plt

g = (g1+g2)/2

you = [0, 50]
them = [0, 0]

xs = []
ys = []

while ((them[0] < 100) and (you[0] <= them[0])):
    xs.append(you[0])
    ys.append(you[1])
    them[0] += .0001
    you = move(you, them, g*.0001)

plt.plot(xs, ys, 'b-')
plt.plot([0, 100], [0, 0], 'r-')
plt.show()
