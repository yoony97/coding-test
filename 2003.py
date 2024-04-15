"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	128 MB	55731	26889	18437	48.334%
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.
"""

def main():
    N, K = [int(i) for i in input().split(" ")]
    arr = [int(i) for i in input().split(" ")]
    answer = 0
    
    #누적합
    csum = [0]*(N+1)
    csum[1] = arr[0]
    for i in range(2,N+1):
        csum[i] = csum[i-1] + arr[i-1]
    
    #투 포인터
    L = 0
    R = 0
    while L<=R:
        if R >= N+1:
            break
        s = csum[R] - csum[L]
        
        if s < K:
            R = R+1
        elif s > K:
            L = L+1
        else:
            answer+=1
            R = R+1

    print(answer)

if __name__ == '__main__':
    main()