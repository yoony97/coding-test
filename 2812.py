"""
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
"""

import sys

data = sys.stdin.read().strip().split("\n")
N, K = map(int, data[0].split())
remain = K
number = data[1]
stack = []

for i in number:
    num = int(i)
    while stack and stack[-1] < num and remain > 0:
        stack.pop()
        remain -= 1
    stack.append(num)

if remain > 0:
    stack = stack[:-remain]
        
print(''.join(map(str, [i for i in stack])))    
                