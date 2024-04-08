"""
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
"""
        
if __name__ == '__main__':
    N, S = [int(i) for i in input().split(" ")]
    arr = [int(i) for i in input().split(" ")]
    sumed_arr = [0]
    for i in range(N):
        sumed_arr.append(sumed_arr[i] + arr[i])
    L = 1
    R = 1
    answer = []
    print(sumed_arr)
    while L <= R and R <= N:
        s = sumed_arr[R] - sumed_arr[L]
        print(L,R,s)
        
        if s >= S:
            L = L + 1
            answer.append(R - L + 1)
        else:
            R = R + 1
    
    if answer:
        print(min(answer))
    else:
        print(0)
                


