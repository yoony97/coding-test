# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
#  0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

#dp[a][b] = sum(dp[a-1][:b])

if __name__ == "__main__":
    T = int(input())
    tc = []

    for _ in range(T):
        a = int(input()) + 1
        b = int(input())
        tc.append((a,b))

    for a,b in tc:
        dp = [[0]*b for _ in range(a)]
        
        for i in range(b): 
            dp[0][i] = i+1
        
        for p in range(1,a):
            for q in range(b):
                dp[p][q] = sum(dp[p-1][:q+1])

        print(dp[a-1][b-1])

