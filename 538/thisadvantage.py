import math
N = 10000

ad = 0
da = 0

for i in range(1, N+1):
    p1 = ((N+1-i)/N)
    p2 = ((N-i)/N)
    pda = (4*(p1**2) - 4*(p1**3) + p1**4) - (4*(p2**2) - 4*(p2**3) + p2**4)
    pad = (2*(p1**2) - p1**4) - (2*(p2**2) - p2**4)
    ad += i*pad
    da += i*pda

print((ad-((7*N)/15) - 1/2)*(N**2))
print((da-((8*N)/15) - 1/2)*(N**2))
