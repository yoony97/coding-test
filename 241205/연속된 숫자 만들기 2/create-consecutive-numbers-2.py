#  A - B - C
#  A - C - B or B - A - C

def check(A,B,C):
    if B - A == 1 and C - B == 1:
        return True
    return False

def dist(A,B):
    return abs(B-A)

def swap(A,B,C):
    return sorted([A,B,C])

A, B, C = map(int, input().split())

dist1 = dist(A,B)
dist2 = dist(B,C)

#항상 큰 값으로 이동하게 만들래
cnt = 0
#for i in range(10):
while not check(A,B,C):
    if check(A,B,C):
        break
    li_A = list(range(A,B+1))
    li_C = list(range(B,C+1))
    if len(li_A) == 0:
        C = li_C[len(li_C)//2]
    elif len(li_C) == 0:
        A = li_A[len(li_A)//2]
    elif len(li_A) > len(li_C):
        A = li_A[len(li_A)//2]
    else:
        C = li_C[len(li_C)//2]
    #print(A,B,C)
    A, B, C = swap(A,B,C)
    #print(A,B,C)
    #print('-----')
    cnt += 1

print(cnt)

