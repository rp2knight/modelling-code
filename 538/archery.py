import random

def getPoint():
    r = 2
    while(r > 1):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        r = x*x + y*y
    return([x, y])

def simulate():
    score = 0
    r = .5
    done = False
    while(not done):
        score += 1
        p = getPoint()
        rp =(p[0]**2 + p[1]**2)
        if (rp > r):
            done = True
        if (rp <= r):
            r = rp
    return(score)
results = []
total = 0
attempts = 10000
m = 0

for i in range(attempts):
    s = simulate()
    results.append(s)
    total += s
    if (s > m):
        m = s
        
display = []

for i in range(m):
    display.append(0)

for i in range(attempts):
    display[results[i]-1] += 1

for i in range(m):
    display[i] = display[i]/attempts

print(total/attempts)
print(display)

circs = 4
simple = []

for i in range(circs):
    ans = circs**(2*i)
    for j in range(i):
        ans += ((2*j+1)*circs**(2*(i-j-1)))*simple[j]
    simple.append(ans)

tot = 0
for i in range(circs):
    tot += ((2*i+1)*(circs**(2*(circs-i))))*simple[i]

print(tot)
print(1+(tot/circs**((circs+1)*2)))

    
