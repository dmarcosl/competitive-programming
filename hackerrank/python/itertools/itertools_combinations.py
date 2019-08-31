from itertools import combinations

data = input().split()
word = data[0]
num = int(data[1])

for i in range(1, num + 1):
    for j in combinations(sorted(word), i):
        print(''.join(j))

