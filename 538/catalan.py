def LexDyckWords(word, zeroes, ones, total):
    word0 = word.copy()
    word0.append(1)
    word1 = word.copy()
    word1.append(-1)
    if (zeroes < total):
        if (ones < total):
            if (zeroes > ones):
                result = LexDyckWords(word0, zeroes+1, ones, total)
                result += LexDyckWords(word1, zeroes, ones+1, total)
            if (zeroes == ones):
                result = LexDyckWords(word0, zeroes+1, ones, total)
        if (ones == total):
            result = LexDyckWords(word0, zeroes+1, ones, total)
            print('hi')
    if (zeroes == total):
        if (ones < total):
            result = LexDyckWords(word1, zeroes, ones+1, total)
        if (ones == total):
            result = [word]
    return result

def DyckWords(total):
    return LexDyckWords([], 0, 0, total)

def TotalTime(word):
    word.append(-1)
    height = 1
    time = 0
    while(len(word) > 0):
        time +=1
        for i in range(height):
            delta = word[0]
            height += delta
            word.remove(delta)
    return time

n = 12
total = 0
count = 0

for word in DyckWords(n):
    count += 1
    total += TotalTime(word)
    if (count % 100 == 0):
        print(count)

print(total, count, total/count)
