words = [input() for _ in range(int(input()))]

repeat = dict()
for w in words:
    if repeat.get(w):
        repeat[w] += 1
    else:
        repeat[w] = 1

print(len(repeat.keys()))
print(' '.join(map(str,repeat.values())))
