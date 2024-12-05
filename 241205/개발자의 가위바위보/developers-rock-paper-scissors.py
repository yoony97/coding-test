# 가위바위보를 한 횟수와 서로 어떤 것을 냈는지 숫자로만 주어질 때,
# 이긴는 횟수가 최대가 되도록 매칭
# 가위 : 1, 바위 : 2, 보 :  3
# 가위 : 1, 바위 : 3, 보 :  2
# 가위 : 2, 바위 : 1, 보 :  3
# 가위 : 2, 바위 : 3, 보 :  1
# 가위 : 3, 바위 : 1, 보 :  2
# 가위 : 3, 바위 : 2, 보 :  1


N = int(input())
matchs = []
for i in range(N):
    a, b = map(int, input().split())
    matchs.append((a,b))

ans = 0
for k in [(1,2,3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]:
    c, r, p  = k #가위 c, 바위 r, 보 p 
    win = 0
    for i in matchs:
        a, b = i 
        if (a == c and b == p):
            win += 1
        elif (a == r and b == c):
            win += 1
        elif (a == p and b == r):
            win += 1
#    print(win)
    ans = max(win, ans)

print(ans)