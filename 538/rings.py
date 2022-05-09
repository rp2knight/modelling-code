import math

n = 50

def shift(f, a):
    output = []
    for i in range(n):
        coeff = 0
        for j in range(n-i):
            coeff += f[i+j]*(a**j)*math.comb(i+j, i)
        output.append(coeff)
    return output

def add(f, g):
    output = []
    for i in range(n):
        output.append(f[i] + g[i])
    return output

def timesx(f):
    output =  [0]
    for i in range(n-1):
        output.append(f[i])
    return output

def evaluate(f, a):
    answer = 0
    for i in range(n):
        answer += (a**i)*f[i]
    return answer

f = [[1]]
zero = [0]
one = [1]

for i in range(1, n):
    f[0].append(0)
    zero.append(0)
    one.append(0)

for i in range(1, n):
    output = zero
    for j in range(1, i):
        output = add(shift(f[j-1], i-j), output)
    output = add(timesx(f[i-1]), output)
    output = add(output, one)
    f.append(output)

for i in range(n):
    print(f[i])

for i in range(2, n):
    print(math.log(evaluate(f[i], 1))/math.log((i**i)))
