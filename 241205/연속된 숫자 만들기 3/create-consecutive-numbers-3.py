#최대 이동 횟수
#두개 다 떨어져있을 경우,
#두 개가 연속할 경우 최대 이동은?
#1, 5, 6
#6을 고르고 연속시킨다. 1, 2, 5
#1를 고르고 연속시킨다. 2, 3, 5
#2를 고르고 연속시킨다. 3, 4, 5
#1, 5, 10
#거리를 짧은 걸 고르고, 연속 시킨다.

pos = list(map(int, input().split()))
count = 0





while (True):
    #print(pos)
    a = abs(pos[0] - pos[1])
    b = abs(pos[1] - pos[2])
    # 각 둘씩 잡아서 거리가 다 1이면 연속한 수
    if a == 1 and b == 1:
        break
    #하나가 연속일 경우 또 연속 만들어주기
    if a == 1 and b > 1:
        pos[0] = pos[1]+1

    elif a > 1 and b == 1:
        pos[2] =  pos[0]+1

    #둘다 거리가  2 이상 일경우, 짧은 걸 골라서 연속시킴
    else:
        if a < b:
            pos[0] = pos[1] + 1
        else:
            pos[2] = pos[0] + 1
    count += 1
    pos.sort()

print(count)
