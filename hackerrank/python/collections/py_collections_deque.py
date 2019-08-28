from collections import deque

d = deque()
for _ in range(int(input())):
    instructions = input().split()
    if instructions[0] == 'append':
        d.append(instructions[1])
    elif instructions[0] == 'appendleft':
        d.appendleft(instructions[1])
    elif instructions[0] == 'pop':
        d.pop()
    elif instructions[0] == 'popleft':
        d.popleft()

print(' '.join(d))

