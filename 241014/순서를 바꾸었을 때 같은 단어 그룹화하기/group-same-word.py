from itertools import permutations
N = int(input())

d = {}

for i in range(N):
    isinclude = False
    string = input()
    for j in permutations(string, len(string)):
        key = ''.join(j)
        if key in d:
            d[key] += 1
            isinclude = True
            break
    if not isinclude:
        d[string] = 1

print(max(d.values()))