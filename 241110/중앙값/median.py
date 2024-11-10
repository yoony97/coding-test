import heapq
#import sys
#input = sys.stdin.read

T = int(input())

def solve(N: int, li: list):
    left = []  # 최대 힙 (중앙값 이하를 저장)
    right = []  # 최소 힙 (중앙값 이상을 저장)
    
    for i in range(N):
        num = li[i]
        
        # 최대 힙에 삽입
        if not left or num <= -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
        
        # 균형 맞추기
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))
        
        # i가 짝수일 때마다 중앙값 출력
        if i % 2 == 0:
            print(-left[0], end=' ')

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    solve(N, li)
    print()