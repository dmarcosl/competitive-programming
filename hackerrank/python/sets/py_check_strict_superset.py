s = set(map(int, input().split()))

for _ in range(int(input())):
    s2 = set(map(int, input().split()))
    if not s >= s2:
        print(False)
        break
        
else:
    print(True)

