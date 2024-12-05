#  A - B - C
#  A - C - B or B - A - C

def check(A,B,C):
    if B - A == 1 and C - B == 1:
        return True
    return False

def check2(A,B,C):
    if B - A == 1 or C - B == 1:
        return True
    return False

def dist(A,B):
    return abs(B-A)

def swap(A,B,C):
    return sorted([A,B,C])

A, B, C = map(int, input().split())


#들어갈 수 있는 후보군 중에서 2번째로 큰 값이 가장 좋아보이는데

cnt = 0
#for i in range(2):
while not check(A,B,C):
    if check(A,B,C):
        break
    elif check2(A,B,C): # 두개가 연속이고 1개가 떨어져있을 경우,
        if B-A == 1:
            li_A = list(range(B+1, C))
            if len(li_A) >= 2:
                A = li_A[-2]
            else:
                A = li_A[0]
        elif C-B == 1:
            li_C = list(range(A+1, B))
            if len(li_C) >= 2:
                C = li_C[-2]
            else:
                C = li_C[0]
    else:
        li_A = list(range(B+1, C))
        li_C = list(range(A+1, B))
        if len(li_A) < len(li_C):
            if len(li_A) < 2:
                A = li_A[0]
            else:
                A = li_A[-2]
        else:
            if len(li_C) < 2:
                C = li_C[0]
            else:
                C = li_C[-2]
    
    A, B, C = swap(A,B,C)
    cnt+= 1
print(cnt)
#case 1: 연속된 수일 경우 패스
#case 2: 5 6 10 두개가 연속되고 한개가 떨어져있을 때,
# 연속된 수 중 끝 값을 선택한다.
# 해당 값을 가운데 넣는다.
# 6 8 10
# 8 9 10
# 이 때, 후보군이 7,8,9 2개 이상일 경우, 2번째로 큰 값을 고른다.
# 이 때, 후보군이 1개 미만일 경우, 그거 고르면 끝


#case 3: 세 숫자 다 떨어져있을 경우,
#1 8 10
#C가 올 수 있는 곳 2, 3, 4, 5, 6, 7
#A가 올 수 있는 곳 9
