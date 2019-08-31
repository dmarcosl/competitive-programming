from itertools import combinations_with_replacement

data = input().split()
word = data[0]
num = int(data[1])

for i in combinations_with_replacement(sorted(word), num):
    print(''.join(i))

