import math

def g(x):
    y = math.pi/x
    z = y/math.tan(y)
    return(math.sqrt(z))

def h(x):
    num = (g(x+1)-g(x))
    den = ((x+1)*g(x+1)-x*g(x))
    return(num/den)

def i(x):
    return((math.pi**2)/(3*(x**3)))

def j(x):
    return(h(x)/i(x))

for k in range(1, 6):
    l = 10**k
    print(l, j(l))
