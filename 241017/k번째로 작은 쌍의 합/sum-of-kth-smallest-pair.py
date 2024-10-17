import heapq
import sys

data = sys.stdin.read().strip().split("\n")

N, M, K = map(int, data[0].split())
A = list(map(int, data[1].split()))
B = list(map(int, data[2].split()))

q = []

for i in range(N):
    for j in range(M):
        total = A[i] + B[j]

        if len(q) < K:
            heapq.heappush(q, (-total, A[i], B[j]))
        else:
            if -q[0][0] > total:
                heapq.heapreplace(q, (-total, A[i], B[j]))
            else:
                break  # B는 정렬되어 있으므로 더 볼 필요 없음

# 최종적으로 K번째 작은 합을 출력
result = -heapq.heappop(q)[0]
print(result)