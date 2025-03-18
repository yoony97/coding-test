n, m = map(int, input().split())
arr = []
relative_blocks_position = [
    [(0,0), (0,1), (0,2), (0,3)], #ㅡ 블록
    [(0,0), (1,0), (2,0), (3,0)],  # ㅡ 블록 회전
    [(0,0), (1,0), (0,1), (1,1)], # ㅁ 블록( 회전 무관 )
    [(0,0), (1,0), (2,0), (2,1)], # ㄴ 블록
    [(0,0), (1,0), (0,1), (0,2)], # ㄴ 블록 오른쪽 90 도 회전
    [(0,0), (0,1), (1,1), (2,1)],  # ㄴ 블록 오른쪽 180도 회전 
    [(0,0), (0,1), (0,2), (-1,2)], # ㄴ 블록 270도 회전
    [(0,0), (1,0), (1,1), (2,0)], # ㅏ 블록
    [(0,0), (0,1), (1,1), (0,2)], # ㅜ
    [(0,0), (1,0), (2,0), (1, -1)], # ㅓ
    [(0,0), (0,1), (1,1), (-1, 1)], # ㅗ
    [(0,0), (1,0), (1,1), (2,1)], # z 블록
    [(0,0), (0,1), (-1,1), (-1,2)] # z 블록 회전
]
for i in range(n):
    inputs = list(map(int, input().split()))
    arr.append(inputs)

answer = 0
for row in range(n):
    for col in range(m):
        for block_position in relative_blocks_position:
            temp = 0
            for y, x in block_position:
                new_row = row + y
                new_col = col + x
                if 0 <= new_row < n and 0 <= new_col < m:
                    temp += arr[new_row][new_col]
                else:
                    temp = -1
                    break
            answer = max(answer, temp)

print(answer)