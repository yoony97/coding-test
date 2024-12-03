N = int(input())
maps = []
for i in range(N):
    maps.append(int(input()))


#언덕 깍기
#최대값 - 최솟값 <= 17
#높이를 올릴 수도, 높이를 깍을 수도 있음
#비용은 x**2
# 최솟값 i로, 최대값을 j:(0, i+17):
# 최솟값이 i가 되도록 설정한다.
# 최대값이 j가 되도록 설정한다.
# 해당 비용을 계산한다.
ans = float('inf')


def make(maps, minimum, maximum):
    #쌓기, 깍기 코스트 최솟값 구하기
    #쌓기 : 전체 언덕을 건드려야함
    lcost = 0
    rcost = 0
    first_cost = 0
    second_cost = 0
    lflag = False
    rflag = False
    for i in range(N):
        if maps[i] < minimum:
            lcost += (minimum - maps[i])**2
            lflag = True
    #깍기: 최솟값만 건드려야함
    if min(maps) > minimum:
        rcost += (minimum - min(maps))**2
        rflag = True
    
    if lflag and rflag:
        first_cost = min(lcost, rcost)
    elif lflag:
        first_cost = lcost
    elif rflag:
        first_cost = rcost

    lcost = 0
    rcost = 0
    
    lflag = False
    rflag = False

    #깍기
    for i in range(N):
        if maps[i] > maximum:
            lcost += (maximum - maps[i])**2
            lflag = True

    #쌓기
    if max(maps) < maximum:
        rcost += (maximum - max(maps))**2
        rflag = True

    if lflag and rflag:
        second_cost = min(lcost, rcost)
    elif lflag:
        second_cost = lcost
    elif rflag:
        second_cost = rcost

    
    return first_cost +  second_cost

ans = float('inf')
for i in range(0, 101):
    for j in range(i, i+18):
        cost = make(maps, i, j)
        #print(cost)
        ans = min(ans, cost)

print(ans)