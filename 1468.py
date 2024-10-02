
"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	11791	5928	4741	50.005%
문제
세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

입력
첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 둘째 줄에는 책의 위치가 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 책의 위치는 0이 아니며, 절댓값은 10,000보다 작거나 같은 정수이다.

출력
첫째 줄에 정답을 출력한다.

"""
import sys
from collections import deque
data = sys.stdin.read().strip().split("\n")

N, M = map(int, data[0].split())

positive = []
negative = []
max_distance = 0

for book in data[1].split():
    book = int(book)
    if book > 0:
        positive.append(book)
    else:
        negative.append(abs(book))

if positive:
    positive.sort(reverse=True)
    max_distance = max(max_distance, positive[0])

if negative:
    negative.sort(reverse=True)
    max_distance = max(max_distance, negative[0])

total_distance = 0

# 음수 방향 이동 거리 계산
for i in range(0, len(negative), M):
    distance = negative[i]
    if distance == max_distance:
        total_distance += distance
    else:
        total_distance += distance * 2

# 양수 방향 이동 거리 계산
for i in range(0, len(positive), M):
    distance = positive[i]
    if distance == max_distance:
        total_distance += distance
    else:
        total_distance += distance * 2

print(total_distance)