#!/usr/bin/python3
a = 1016
mult = 2**(4*a)
def f(x):
    return (x+mult)**(a+1) - x*(x+2*mult)**a
lo = 2**(2*a)
hi = lo + 1
assert f(lo) > 0
while f(hi) > 0:
    hi += hi - lo
while hi - lo > 1:
    print('.', end='', flush=True)
    mid = (hi + lo) >> 1
    if f(mid) > 0:
        lo = mid
    else:
        hi = mid
print('')
print(bin(lo))
print(bin(hi))