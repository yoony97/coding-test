n = int(input())

current = 0
li = []
offset = float('inf')

for _ in range(n):
    x, direct = input().split()
    x = int(x)
    li.append((x, direct))
    if direct =='L':
        x = -x
    current += x
    offset = min(current, offset)

ans = [0]*1000
current = abs(offset)
for x, direct in li:
    if direct == 'R':
        for i in range(current, current+x):
            ans[i] += 1
        current = current+x
    else:
        for i in range(current, current-x, -1):
            ans[i] += 1
        current = current - x

cnt = 0


for i in ans:
    if i >= 2:
        cnt += 1

print(cnt)
