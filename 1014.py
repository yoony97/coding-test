"""
최백준은 서강대학교에서 “컨닝의 기술”이라는 과목을 가르치고 있다. 
이 과목은 상당히 까다롭기로 정평이 나있기 때문에, 몇몇 학생들은 시험을 보는 도중에 다른 사람의 답지를 베끼려 한다.

시험은 N행, M열 크기의 직사각형 교실에서 이루어진다. 
교실은 1×1 크기의 단위 정사각형으로 이루어져 있는데, 각 단위 정사각형은 자리 하나를 의미한다.

최백준은 컨닝을 방지하기 위해서 다음과 같은 전략을 세웠다. 
모든 학생은 자신의 왼쪽, 오른쪽, 왼쪽 대각선 위, 오른쪽 대각선 위, 이렇게 총 네 자리에 앉아있는 친구의 답지를 항상 베낀다고 가정한다. 
따라서, 자리 배치는 모든 학생이 컨닝을 할 수 없도록 배치되어야 한다.


위의 그림을 보자. A, C, D 혹은 E에 다른 학생을 앉히는 것은 좋은 생각이 아니다. 
그 이유는 이미 앉아있는 학생이 그들의 답안지를 베낄 우려가 있기 때문이다. 하지만, B에 다른 학생을 앉힌다면, 두 학생은 서로의 답지를 베낄 수 없어 컨닝의 우려가 없다.

위와 같이 컨닝이 불가능하도록 자리를 배치 하려는 최백준의 행동에 분노한 일부 학생들이 교실의 책상을 부숴버렸기 때문에, 일부 자리에는 학생이 앉을 수 없다.

최백준은 교실의 모양이 주어졌을 때, 이 곳에서 아무도 컨닝을 할 수 없도록 학생을 배치하였을 경우에 교실에 배치할 수 있는 최대 학생 수가 몇 명인지 궁금해졌다. 최백준을 위해 이를 구하는 프로그램을 작성하라.
"""

C = int(input())
answer = []


def valid_sequence(n,blocked):
    # n 비트 길이에서 가능한 모든 숫자를 반복
    blocked_mask = sum(1 << (n - 1 - pos) for pos in blocked)
    for i in range(2 ** n):
        if i & blocked_mask != 0:
            continue  # 블록된 위치 중 하나라도 '1'이면 이 숫자는 건너뜀
        # 현재 숫자 i가 '1'이 연속되지 않는지 확인
        if (i & (i >> 1)) == 0:
            # 연속된 '1'이 없다면, 비트 문자열로 변환
            yield int(f'{i:0{n}b}',2)

def generate_non_consecutive_bit_strings(N, blocked):
    return list(valid_sequence(N, blocked))


def max_students_with_desks(grid):
    N = len(grid)    # 행의 수
    M = len(grid[0]) # 열의 수
    
    def valid_position(mask, row):
        return (mask & (mask >> 1)) == 0 and (mask & row) == mask

    # 가능한 마스크를 각 행별로 계산
    row_masks = []
    for i in range(N):
        row = 0
        for j in range(M):
            if grid[i][j] == '.':
                row |= (1 << (M - 1 - j))
        row_masks.append(row)

    valid_masks = []
    dp = [[0] * (1 << M) for _ in range(N + 1)]

    for i in range(N):
        valid_masks.append([])
        for mask in range(1 << M):
            if valid_position(mask, row_masks[i]):
                valid_masks[i].append(mask)
    
    for i in range(1, N + 1):
        for curr_mask in valid_masks[i-1]:
            for prev_mask in valid_masks[i-2] if i > 1 else [0]:
                if (curr_mask & (prev_mask >> 1)) == 0 and (curr_mask & (prev_mask << 1)) == 0:
                    dp[i][curr_mask] = max(dp[i][curr_mask], dp[i-1][prev_mask] + bin(curr_mask).count('1'))
    
    return max(dp[N])

for i in range(C):
    N, M = map(int, input().split(" "))
    arr = []
    max_len = int('0b'+'1'*M, 2)
    dp = [[0] * (1 << M) for _ in range(N + 1)]


    #print(max_len)
    for c in range(N):
        s = input()
        arr.append([i for i in s])
        
    print(max_students_with_desks(arr)) 