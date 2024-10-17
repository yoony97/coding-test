import heapq
import copy

N = int(input())
numbers = list(map(int, input().split()))
q = []

# for i in numbers:
#     heapq.heappush(q, -i)

maximum = 0

for K in range(1, N-1):
    q = []
    for i in numbers[K:]:
        heapq.heappush(q, i)
    heapq.heappop(q) 
    maximum = max(maximum, (sum(q)/len(q)))

print(format(maximum, '.2f'))
"""
N개의 정수들이 있습니다. 
이 중 정확히 앞에서부터 K개를 삭제하고 난 후, 남아있는 정수 중 가장 작은 숫자 하나를 제외한 평균을 구한다 했을 때 
이 평균값이 최대가 될 때의 값을 구하는 프로그램을 작성해보세요. 단, K는 1이상 N - 2 이하까지만 고려하도록 합니다.
"""