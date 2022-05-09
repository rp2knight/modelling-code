import matplotlib.pyplot as plt

def f(x):
    return((2 - x**4 - (1-x)**4)/4)

xmin = 0
xmax = 1
ymin = 0
ymax = 1
accuracy = 10000

xvalues = []
yvalues = []

for i in range(accuracy+1):
    x = xmin + (i*(xmax-xmin))/accuracy
    xvalues.append(x)
    yvalues.append(f(x))

plt.plot(xvalues, yvalues, 'r-')
plt.plot([xmin, xmax], [ymin, ymax], ' ')
plt.show()
