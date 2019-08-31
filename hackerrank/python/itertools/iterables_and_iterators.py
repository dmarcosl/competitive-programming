from itertools import combinations

input()
l = input().split()
k = int(input())

combs = list(combinations(l, k))
f = filter(lambda c: 'a' in c, combs)
print(round(len(list(f)) / len(combs), 3))

