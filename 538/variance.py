import math
import numpy as np
import matplotlib.pyplot as plt

n = 1000
p = 1000000
tp = 0
prob = []
var = 0
for i in range(p):
    tp += (i**(n//2))*(((p-i)**(n//2)))
for j in range(p):
    prob.append(((j**(n//2))*((p-j)**(n//2)))/(tp))
for k in range(p):
    var += prob[k]*((k/p)**2)
var -= 1/4
print(var)
print(1/(4*(n+3)))
x = (math.comb(n, n//2)*(n+1))
#for l in range(p):
#    plt.plot((l/p), prob[l]*(p+1), "b.")
#    plt.plot((l/p), (((l*(p-l))/(p*p))**(n//2))*x, "r.")
#plt.show()
