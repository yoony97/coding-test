from sortedcontainers import SortedSet

n, m = map(int, input().split())
removed_coordinate = set()
# 전체 구간을 초기화
s = SortedSet([(-(0), n)])

# 제외할 좌표 리스트 입력받기
li = list(map(int, input().split()))

for i in li:
    # 이미 제거된 좌표는 무시
    if i in removed_coordinate:
        continue
    
    # 좌표 제거 추가
    removed_coordinate.add(i)
    
    # i가 포함된 구간 찾기
    idx = s.bisect_right((-i, n))
    if idx >= len(s):
        continue  # 유효한 구간이 아니면 건너뜀
    
    # 현재 구간의 시작과 끝 확인
    start, end = -s[idx][0], s[idx][1]
    
    # i를 포함한 구간이 맞는지 확인
    if not (start <= i <= end):
        continue
    
    # 구간 삭제 및 새로운 구간 추가
    s.remove(s[idx])
    
    # i를 기준으로 두 구간으로 나눔
    if start < i:
        s.add((-(start), i - 1))  # 왼쪽 구간 추가
    if i < end:
        s.add((-(i + 1), end))  # 오른쪽 구간 추가

    print(max([i[1]+i[0]+1 for i in s]))