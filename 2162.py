"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	17428	5302	3659	28.660%
문제
N개의 선분들이 2차원 평면상에 주어져 있다. 선분은 양 끝점의 x, y 좌표로 표현이 된다.

두 선분이 서로 만나는 경우에, 두 선분은 같은 그룹에 속한다고 정의하며, 그룹의 크기는 그 그룹에 속한 선분의 개수로 정의한다. 
두 선분이 만난다는 것은 선분의 끝점을 스치듯이 만나는 경우도 포함하는 것으로 한다.

N개의 선분들이 주어졌을 때, 이 선분들은 총 몇 개의 그룹으로 되어 있을까? 
또, 가장 크기가 큰 그룹에 속한 선분의 개수는 몇 개일까? 이 두 가지를 구하는 프로그램을 작성해 보자.

입력
첫째 줄에 N(1 ≤ N ≤ 3,000)이 주어진다. 
둘째 줄부터 N+1번째 줄에는 양 끝점의 좌표가 x1, y1, x2, y2의 순서로 주어진다. 
각 좌표의 절댓값은 5,000을 넘지 않으며, 입력되는 좌표 사이에는 빈칸이 하나 있다.

출력
첫째 줄에 그룹의 수를, 둘째 줄에 가장 크기가 큰 그룹에 속한 선분의 개수를 출력한다.

예제 입력 1 
"""
import sys
from collections import deque
from collections import Counter


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def on_segment(p1, p2, p):
    """ 점 p가 선분 p1-p2 위에 있는지 확인하는 함수 """
    return min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])

def is_intersect(A1, A2, B1, B2):
    ccw1 = ccw(A1, A2, B1)
    ccw2 = ccw(A1, A2, B2)
    ccw3 = ccw(B1, B2, A1)
    ccw4 = ccw(B1, B2, A2)
    
    # 두 선분이 교차하는 일반적인 경우
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True
    
    # 경계에 있는 경우 처리
    if ccw1 == 0 and on_segment(A1, A2, B1):
        return True
    if ccw2 == 0 and on_segment(A1, A2, B2):
        return True
    if ccw3 == 0 and on_segment(B1, B2, A1):
        return True
    if ccw4 == 0 and on_segment(B1, B2, A2):
        return True
    
    return False

data = sys.stdin.read().strip().split("\n")
N = int(data[0])
lines = [list(map(int,i.split(" "))) for i in data[1:]]

parent = [i for i in range(N)]


def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b: 
        if a < b:
            parent[b] = a
        else:
            parent[a] = b



for i in range(N):
    if parent[i] != -1:
        A1, A2 = (lines[i][0], lines[i][1]) , (lines[i][2], lines[i][3])
        for j in range(i, N):
            B1, B2 = (lines[j][0], lines[j][1]) , (lines[j][2], lines[j][3])
            if is_intersect(A1, A2, B1, B2):
                union(i,j)

# 그룹을 최신화한 후, 그룹별로 카운트를 셉니다.
group_count = Counter(find(i) for i in range(N))

# 그룹의 수와 가장 큰 그룹의 크기를 출력합니다.
print(len(group_count))
print(max(group_count.values()))