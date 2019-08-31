from itertools import permutations

data = input().split()
word = data[0]
num = int(data[1])

perms = list(permutations(word, num))
perms.sort()

[print(''.join(t)) for t in perms]

