OFFSET = 100
MAX_R = 200
li = [[0]*MAX_R for i in range(MAX_R)]
n = int(input())

def fill(x1,y1):
    for i in range(x1, x1 + 8):
        for j in range(y1, y1 + 8):
            li[i][j] = 1

for i in range(n):
    x1, y1 = map(int, input().split())
    fill(x1+OFFSET, y1+OFFSET)

ans = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            ans += 1

print(ans)