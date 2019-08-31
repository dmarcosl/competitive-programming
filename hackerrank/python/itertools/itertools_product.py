from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = list(product(a, b))

[print(t, end=' ') for t in l]

