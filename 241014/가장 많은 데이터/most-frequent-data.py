n = int(input())

d = dict()
for i in range(n):
    s = input()
    if s not in d:
        d[s] = 0
    d[s] += 1

print(max([d[i] for i in d]))