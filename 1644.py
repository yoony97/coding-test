"""
문제
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

출력
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
"""


import math

def get_prime(n):
    array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)
    prime = []
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(2,n+1):
        if array[i]:
            prime.append(i)

    return prime
    
if __name__ =='__main__':
    N = int(input())
    L, R = 0, 0
    answer = 0 
    
    prime = get_prime(N)
    arr = [0]*(len(prime)+1)

    
    for i in range(1,len(prime)+1):
        arr[i] = arr[i-1] + prime[i-1]

    while L <= R:
        if R >= len(arr):
            break
        s = arr[R] - arr[L]
        if s < N:
            R = R+1
        elif s > N:
            L = L+1
        else:
            answer += 1
            L = L+1
    print(answer)