import math

acc = .00000001
x = 0
y = math.atan(x) + math.pi
while (abs(y-x) > acc):
    x = y
    y = math.atan(x) + math.pi
    print(x)

print(x, x/math.pi)
