N, K = map(int, input().split())
li = [0]*N
for _ in range(K):
    A, B = map(int, input().split())
    for i in range(A-1,B):
        li[i] += 1

print(max(li))