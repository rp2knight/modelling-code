def ToChars(str):
    return list(str)

def MackerelMatch(state, word):
    ret = True
    lets = ToChars(state.lower())
    letw = ToChars(word.lower())
    for i in range(len(lets)):
        for j in range(len(letw)):
            if lets[i] == letw[j]:
                ret = False
    return(ret)

s = 'álava'

f = open('germanstates.txt', 'w')
f.write('BadenWürttemberg\nBayern\nBerlin\nBrandenburg\nBremen\nHamburg\nHesse\nNiedersachsen\nMecklenburgVorpommern\nNordrheinWestfalen\nRheinlandPfalz\nSaarland\nSachsen\nSachsenAnhalt\nSchleswigHolstein\nThüringen\n')
##s = f.readline()
##print(s)
