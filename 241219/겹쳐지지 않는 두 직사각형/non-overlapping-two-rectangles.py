n, m = map(int, input().split())
maps =[]

for _ in range(n):
    maps.append(list(map(int, input().split())))

#직사각형 선택하기 프로젝트
#직사각형 두개 고르자.
# 모든 직사각형 좌표 저장
arr = []
for sy in range(n):
    for sx in range(m):
        for ey in range(sy, n):
            for ex in range(sx, m): 
                arr.append((sy, sx, ey, ex))

ans = -float('inf')
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        ay1, ax1, ay2, ax2 = arr[i]
        by1, bx1, by2, bx2 = arr[j]
        #두개가 겹치나?
        if (
            ay2 < by1 or by2 < ay1 or ax2 < bx1 or bx2 < ax1
        ):
            a = 0
            b = 0
            for p in range(ay1, ay2+1):
                for q in range(ax1, ax2+1):
                    a += maps[p][q]
            
            for p in range(by1, by2+1):
                for q in range(bx1, bx2+1):
                    b += maps[p][q]
            ans = max(a+b, ans)

print(ans)