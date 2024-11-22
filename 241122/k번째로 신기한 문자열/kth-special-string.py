
n, k, T = input().split()
n, k = int(n), int(k)
li = []
for _ in range(n):
    s = input()
    if s.startswith(T):
        li.append(s)

li.sort()
print(li[k-1])
