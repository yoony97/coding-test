import heapq

N, M, K = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
q = []
for i in arr1:
    for j in arr2:
        heapq.heappush(q, (i+j, i,j))

for i in range(K):
    s, x, y = heapq.heappop(q)

print(s)