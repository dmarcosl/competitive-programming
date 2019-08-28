from collections import OrderedDict

d = OrderedDict()

for _ in range(int(input())):
    inp = input()
    name = inp[:inp.rfind(' ')]
    value = int(inp[inp.rfind(' ') + 1:])
    d[name] = d.get(name, 0) + value

[print('{} {}'.format(name, value)) for name, value in d.items()]

