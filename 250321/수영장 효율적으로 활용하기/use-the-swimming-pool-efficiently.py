n, m = map(int, input().split())
T = list(map(int, input().split()))

# Please write your code here.

#1번 레일에 몇명 끊고
#2번 레일에 몇명 끊고
#n번 레일에 몇명 끊어서
# 레이별 수영장 이용시간의 합들 중 최대값이 최솟값이 되는 경우를 찾는 것
# 칸막이 개수가 m개 느낌이네

left = 0
right = sum(T)


def ispossible(mid, m):
    count = 1
    sum_eval = 0
    for time in T:
        if time > mid:#  한사람이 최대값보다 넘은 경우 바로 중단
            return False
        sum_eval += time
        if sum_eval > mid:
            count += 1
            sum_eval = time

    return count <= m

answer = float('inf')

while left <= right:
    mid = (left+right)//2  #해당 이용시간보다 크니 작니로 해야겠네

    if ispossible(mid, m): #해당 이용시간의 최대값 mid가 가능하면 좀더 줄여보자.
        right = mid-1
        answer = min(mid, answer)
    else:
        left = mid+1


print(answer)
    

