  # N번 : a <-> b
  # c번 종이컵 열어 조약돌이 있으면 점수 업ㄷ음



N = int(input())
action = []
ans = 0

for i in range(N):
    a, b, c = map(int,input().split())
    action.append((a,b,c))

for i in range(3): #조약돌 위치 i
    current = [0]*3
    current[i] = 1
    score = 0
    for l in range(N):
        a, b, c = action[l]
        current[a-1], current[b-1] = current[b-1], current[a-1]
        if current[c-1] == 1:
            score += 1  
    ans = max(ans, score)

print(ans)