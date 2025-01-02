#동전을 수집할 시에는 꼭 번호가 증가하는 순서대로 수집해야만 합니다. 
#또, 해당 위치를 지나가더라도 동전을 수집하지 않아도 되며 같은 위치를 2번 이상 지나가는 것 역시 허용됩니다.
import sys
import math
sys.setrecursionlimit(50000)

N = int(input())
start = None
end = None
bag = []
ans = float('inf')
coins = []


for row in range(N):
    temp = list(map(str, input()))
    for col in range(N):
        if temp[col] == 'S':
            start = (row, col)
        elif temp[col] == 'E':
            end  = (row, col)
        elif temp[col] != '.':
            coins.append((int(temp[col]), row, col))

def get_distance(s1, s2):
    r1, c1 = s1
    r2, c2 = s2
    return abs(r1-r2) + abs(c1-c2)

visited =  [False]*len(coins)

def solve(current_point, distance):
    global ans
    if len(coins) < 3:
        return
    
    if len(bag) >= 3:
        ans = min(ans, distance + get_distance(current_point, end))
        return
    
    for i in range(len(coins)):
        if (len(bag) == 0 or bag[-1] < coins[i][0]):
            if not visited[i]:
                bag.append(coins[i][0])
                visited[i] = True
                solve((coins[i][1],coins[i][2]), distance + get_distance(current_point, (coins[i][1],coins[i][2])))
                bag.pop()
                visited[i] = False
                #solve((coins[i][1],coins[i][2]), distance + get_distance(current_point, (coins[i][1],coins[i][2])))

solve(start, 0)
if ans == float('inf'):
    print(-1)
else:
    print(ans)