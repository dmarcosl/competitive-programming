k = int(input())
array = list(map(int, input().split()))

s = (sum(set(array)) * k - sum(array)) // (k - 1)

print(s)

