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
while True:
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
