input()
m = set(map(int, input().split()))
input()
n = set(map(int, input().split()))

sim_dif = list(m ^ n)
sim_dif.sort()

print('\n'.join([str(i) for i in sim_dif]))

