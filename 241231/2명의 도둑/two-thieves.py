N, M, C = map(int, input().split())
maps = []
coordinates = []
target = []
answer =  0
for _ in range(N):
    maps.append(list(map(int, input().split())))

def continuous(p1, p2):
    #같은 행을 골랐을 때에는 선택한 M개의 열이 서로 겹쳐서는 안됩니다.
    r1, c1 = p1
    r2, c2 = p2
    if r1 == r2:
        min_c = min(c1, c2)
        max_c = max(c1, c2)
        if (min_c + M >= max_c):
            return False
    return True

def get_weight(p):
    r, c = p
    result = []
    
    for i in range(M):
        if not (0 <= c + i < N):
            return []
        result.append(maps[r][c+i])
    
    if sum(result) > C:
        result.sort()
        while sum(result) > C:
            result.pop(0)

    return result

for i in range(N):
    for j in range(N):
        coordinates.append((i,j))

def solve(cur_num, target, coordinates):
    global answer
    if len(target) == 2:
        coord1, coord2 = target[0], target[1]
        if continuous(coord1, coord2):
            temp = 0
            for i in get_weight(coord1):
                temp += i * i

            for i in get_weight(coord2):
                temp += i * i

            answer = max(answer, temp)
        return

    if cur_num >= len(coordinates):
        return

    
    target.append(coordinates[cur_num])
    solve(cur_num + 1, target, coordinates)
    target.pop()

    # 현재 좌표를 선택하지 않는 경우
    solve(cur_num + 1, target, coordinates)

                

solve(0, target,  coordinates)
print(answer)
