def count_papers(x, y, size):
    # 기준 색상 확인
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                # 하나라도 다른 색상이 있으면 분할
                mid = size // 2
                count_papers(x, y, mid)
                count_papers(x, y + mid, mid)
                count_papers(x + mid, y, mid)
                count_papers(x + mid, y + mid, mid)
                return
    # 모든 색상이 같으면 카운트 증가
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

# 입력 처리
N = int(input().strip())  # 종이의 크기
paper = [list(map(int, input().strip().split())) for _ in range(N)]

# 결과를 저장할 배열
result = [0, 0]  # [하얀색 색종이 수, 파란색 색종이 수]

# 분할 시작
count_papers(0, 0, N)

# 결과 출력
print(result[0])
print(result[1])
