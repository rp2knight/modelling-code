high = 1000000
values = []

for i in range(high):
    values.append(2.54*i)

for i in range(1, high):
    for j in range(high//i + 1):
        if (j*i < high):
            values[i*j] = values[i*j]-i

successes = []
for i in range(high):
    if (-.5 < values[i] < .5):
        successes.append(i)

print(successes)
