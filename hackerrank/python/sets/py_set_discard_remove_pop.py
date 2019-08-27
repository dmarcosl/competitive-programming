n = int(input())
s = set(map(int, input().split()))

for line in range(int(input())):
    instructions = input().split()

    if instructions[0] == 'pop':
        s.pop()
    elif instructions[0] == 'remove':
        s.remove(int(instructions[1]))
    elif instructions[0] == 'discard':
        s.discard(int(instructions[1]))

print(sum(s))

