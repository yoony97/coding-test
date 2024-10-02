import sys
input = sys.stdin.readline

def solve():
    T = int(input())  # 테스트 케이스의 수
    for _ in range(T):
        n = int(input())  # n개의 스티커
        sticker = [list(map(int, input().split())) for _ in range(2)]
        
        if n == 1:
            # 스티커가 한 열밖에 없으면, 더 큰 값을 출력
            print(max(sticker[0][0], sticker[1][0]))
            continue
        
        # DP 테이블 생성
        dp = [[0] * n for _ in range(2)]
        
        # 첫 번째 열은 각각의 스티커를 선택하는 경우로 초기화
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        
        if n > 1:
            # 두 번째 열은 첫 번째 열과 비교
            dp[0][1] = sticker[0][1] + dp[1][0]
            dp[1][1] = sticker[1][1] + dp[0][0]
        
        # DP 점화식에 따라 최대 점수 계산
        for i in range(2, n):
            dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
        
        # 마지막 열에서의 최대값을 출력
        print(max(dp[0][n-1], dp[1][n-1]))

# 입력을 받아서 문제 해결 함수 호출
solve()
