from collections import namedtuple

n = int(input())
mark = namedtuple('mark', input().split())

l = [mark(*input().split()) for _ in range(n)]

print(sum([int(m.MARKS) for m in l]) / len(l))

