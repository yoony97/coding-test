from collections import deque
import copy

def rotate(cp, degree, arr):
    """
    회전 목표: 
        1. 유물 1차 획득 가치를 최대화
        2. 여러 방법일 경우 회전 각도가 가장 작은 방법
        3. 회전 중심 좌표의 열이 가장 작은 구간
        4. 회전 중심 좌표의 행이 가장 작은 구간
    """
    # 원본 배열 복사 (깊은 복사)
    new_arr = [row.copy() for row in arr]
    x, y = cp

    # 회전할 3×3 부분 배열 추출
    temp = [ [ new_arr[i][j] for j in range(y-1, y+2)] for i in range(x-1, x+2) ]

    # degree 값에 따라 90°, 180°, 270° 회전 (시계방향)
    if degree == 0:
        temp = [list(reversed(col)) for col in zip(*temp)]
    elif degree == 1:
        temp = [list(reversed(col)) for col in zip(*temp)]
        temp = [list(reversed(col)) for col in zip(*temp)]
    elif degree == 2:
        temp = [list(reversed(col)) for col in zip(*temp)]
        temp = [list(reversed(col)) for col in zip(*temp)]
        temp = [list(reversed(col)) for col in zip(*temp)]

    # 회전한 부분을 복사한 배열에 반영
    for i, row in enumerate(range(x-1, x+2)):
        for j, col in enumerate(range(y-1, y+2)):
            new_arr[row][col] = temp[i][j]
    return new_arr

def chain(arr):
    """
    인접하여 같은 숫자가 3개 이상이면 해당 셀들을 -1로 변환하고,
    그 개수를 점수로 반환한다.
    
    반환 값:
      (총 점수, 제거된 셀들의 좌표 리스트, 업데이트된 배열)
    """
    # arr 복사본 생성 (원본을 직접 변경하지 않기 위해)
    new_arr = [row.copy() for row in arr]
    visited = [[False]*5 for _ in range(5)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    total_score = 0
    removal_positions = []  # -1로 변경할 좌표들을 저장

    for col in range(5):
        for row in range(5):
            if visited[row][col]:
                continue
            # 이미 제거된 셀은 건너뜁니다.
            if new_arr[row][col] == -1:
                visited[row][col] = True
                continue
            group = [(row, col)]
            q = deque([(row, col)])
            visited[row][col] = True
            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr = r + dx[i]
                    nc = c + dy[i]
                    if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and new_arr[r][c] == new_arr[nr][nc]:
                        q.append((nr, nc))
                        group.append((nr, nc))
                        visited[nr][nc] = True
            if len(group) >= 3:
                total_score += len(group)
                removal_positions.extend(group)

    # 3개 이상 인접한 그룹을 -1로 변환
    for (r, c) in removal_positions:
        new_arr[r][c] = -1

    return total_score, removal_positions, new_arr

def fill(result, added, arr):
    """
    result에 해당하는 좌표에 added 리스트의 값을 채워넣어
    -1 상태인 셀들을 갱신한다.
    
    반환 값:
      (사용 후 남은 added 리스트, 업데이트된 배열)
    """
    new_arr = [row.copy() for row in arr]
    # 좌표를 (열, 행) 기준으로 정렬
    result.sort(key=lambda x: (x[1], -x[0]))
    target = 0
    for i in added[:len(result)]:
        x, y = result[target]
        new_arr[x][y] = i
        target += 1
    added = added[target:]
    return added, new_arr

def simulate(added, arr):
    max_score = -1
    info = (-1, -1, -1)
    max_result = []
    best_arr = None
    # 최대 점수를 주는 회전 구하기 (원본 arr은 그대로 유지)
    for degree in range(3):
        for cx in range(1, 4):
            for cy in range(1, 4):
                temp_arr = rotate((cx, cy), degree, arr)
                score, result, updated_arr = chain(temp_arr)
                if score > max_score:
                    info = (degree, cx, cy)
                    max_score = score
                    max_result = result
                    best_arr = updated_arr
    # 회전 가능한 그룹이 없으면 -1 반환
    if max_score == -1 or len(max_result) == 0:
        return -1

    total_score = 0
    max_d, max_cx, max_cy = info
    # 최대 점수를 주는 회전을 원본 arr에 적용 (새 배열 반환)
    arr = rotate((max_cx, max_cy), max_d, arr)
    score, result, arr = chain(arr)
    total_score += score

    added, arr = fill(result, added, arr)  # -1 셀 채우기
    s, result, arr = chain(arr)  # 연쇄 확인 (이미 채워진 셀은 새로운 체인으로 인식되지 않음)
    total_score += s
    while s > 0:
        added, arr = fill(result, added, arr)
        s, result, arr = chain(arr)
        total_score += s

    return (added, total_score, arr)


# 메인 실행 부분
arr = []
K, M = map(int, input().split())
for i in range(5):
    arr.append(list(map(int, input().split())))
added = list(map(int, input().split()))

answer = 0
for i in range(K):
    sim_result = simulate(added, arr)
    if sim_result == -1:
        break
    added, total_score, arr = sim_result
    print(total_score, end = ' ')
