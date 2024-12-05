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

while not check(A,B,C):
    if check(A,B,C):
        break
    if dist1 > dist2:
        A = (C+B)//2
    else:
        C = (A+B)//2
    A, B, C = swap(A,B,C)
    #print(A,B,C)
    cnt += 1

print(cnt)


