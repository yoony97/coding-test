n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

L = [0]*(n+1)
R = [0]*(n+1)
for i in range(n):
    L[i+1] = max(L[i], arr[i])

for idx, i in enumerate(arr[::-1]):
    R[idx+1] = max(R[idx], i)

R = list(reversed(R))






for a,b in queries:

    left = a-2
    right = b

    print(max(L[left], R[right]))
