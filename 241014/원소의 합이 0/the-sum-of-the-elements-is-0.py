N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

diff_1 = {}
diff_2 = {}
for i in range(N):
    for j in range(N):
        res = A[i] + B[j]
        if res in diff_1:
            diff_1[res] += 1
        else:
            diff_1[res] =1

for i in range(N):
    for j in range(N):
        res = C[i] + D[j]
        if res in diff_2:
            diff_2[res] += 1
        else:
            diff_2[res] =1

answer = 0
for d1 in diff_1:
    for d2 in diff_2:
        if d1 + d2 == 0:
            answer += (diff_1[d1] + diff_2[d2])


print(answer//2)