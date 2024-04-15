"""
입력
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다. N은 2 이상 100,000 이하이다. 두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다. 둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.

출력
첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.
"""

def main():
    N, K = [int(i) for i in input().split(" ")]
    temp = [int(i) for i in input().split(" ")]
    sumarr = [0] * N
    sumarr[0] = temp[0]
    
    for i in range(1,N):
        sumarr[i] = sumarr[i-1] + temp[i]
    maximum = sumarr[K-1]
    L = 0
    R = K

    while R < N:
        s = sumarr[R] - sumarr[L]
        if maximum < s:
            maximum = s
        L+=1
        R+=1

    print(maximum)


if __name__ == '__main__':
    main()