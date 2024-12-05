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
#for i in range(2):
while not check(A,B,C):
    if check(A,B,C):
        break
    li_A = list(range(A+1,B))
    li_C = list(range(B+1,C))
    if len(li_A) == 0:
        A = li_C[len(li_C)//2]
    elif len(li_C) == 0:
        C = li_A[len(li_A)//2]
    
    elif len(li_A) < len(li_C):
        C = li_A[len(li_A)//2]
    else:
        A = li_C[len(li_C)//2]
    # print(li_A, li_C)
    # print(A,B,C)
    A, B, C = swap(A,B,C)
    # print(A,B,C)
    # print('-----')
    cnt += 1
print(cnt)


#5,6 / 8
