"""
1부터 N까지의 자연수가 차례로 적혀 있는 배열이 있다. 아래의 배열은 N=6인 경우의 예이다.

1	2	3	4	5	6
이러한 배열에서 임의의 구간 (a, b)를 잡아, 그 구간에 포함되는 수들을 회전시킬 수 있다. 회전을 하게 되면 a번째 칸부터 b번째 칸까지 적혀 있는 수의 순서가 뒤집히고, 부호 또한 바뀌게 된다. (1 ≤ a ≤ b ≤ N) 예를 들어 위의 배열에서 (1, 4)에서 회전을 수행한 결과는 아래와 같이 된다.

-4	-3	-2	-1	5	6
이미 회전을 수행한 배열에 대해서도 물론 계속 회전을 수행할 수 있다. 다시 (3, 5)에서 회전을 수행하면 최종 배열 상태는 아래와 같이 된다.

-4	-3	-5	1	2	6
초기 배열에는 1부터 N까지의 자연수가 차례로 적혀 있다. 최종 배열 상태가 주어졌을 때 가급적 적은 횟수의 회전 연산을 수행하여 초기 배열에서 최종 배열을 만드는 프로그램을 작성하시오.
"""




import random
from collections import deque


def rotate(arr, start, end):
    return arr[:start] + [-x for x in reversed(arr[start:end + 1])] + arr[end + 1:]


def find_array(arr):
    start, end = 0, 0
    temp_start, temp_end = 0, 0
    
    for i in range(len(arr) - 1):
        if abs(arr[i]) <= abs(arr[i + 1]):
            temp_end = i + 1
        else:
            if temp_end - temp_start > end - start:
                start, end = temp_start, temp_end
            temp_start, temp_end = i + 1, i + 1
    
    if temp_end - temp_start > end - start:
        start, end = temp_start, temp_end
    return list(range(start, end + 1))


def solve():
    N = int(input())
    final_array = [int(i) for i in input().split(" ")]
    for i in range(10):
        if not is_sorted(final_array):
            break
        target = find_array(final_array)
        print(target)
        final_array = rotate(final_array, min(target), max(target))
        print(final_array)

    
def is_sorted(arr):
    return [arr[i-1] <= arr[i] for i in range(1,len(arr))]

if __name__ == '__main__':
    solve()



"""
[1, 2, 3, 4, 5, 6, 7]
[1 -6 -5 -4 -3 -2 7]
[1 6 5 4 3 2 7]
#내림 차순 안되는 부분
#[2,5]
#
"""


