X, Y = map(int, input().split())
cnt = 0
for num in range(X,Y+1):
    temp = list(map(str, str(num)))
    temp = ''.join(temp[::-1])
    if str(num) == temp:
        cnt += 1

print(cnt)