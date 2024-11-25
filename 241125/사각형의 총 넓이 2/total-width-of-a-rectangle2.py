offset = 100
MAX_R = 200
li = [[0]*MAX_R for _ in range(MAX_R)]
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            li[i+offset][j+offset] = 1
ans = 0

for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            ans += 1
    

print(ans)