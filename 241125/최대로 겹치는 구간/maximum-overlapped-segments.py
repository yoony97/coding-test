n = int(input())
mini = float('inf')
maxi = 0
li = []

for _ in range(n):
    A, B = map(int, input().split())
    li.append((A,B))
    mini = min(A,B,mini)
    maxi = max(A,B,maxi)


ans = [0]*(maxi-mini+1)

#print(ans, mini, maxi)
for A,B in li:
    for i in range(A,B):
        ans[i - mini] += 1


print(max(ans))
