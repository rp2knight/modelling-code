f = open('francais.txt', 'r')
o = open('french.txt', 'w')
for line in f:
    l = list(line)
    out = ''
    done = False
    for i in range(len(l)):
        if (l[i] == ' '):
            done = True
            out += '\n'
        else:
            if not done:
                out += l[i]
    o.write(out)
