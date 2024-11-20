_ = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
isSub = True
if B[0] in A:
    idx = A.index(B[0])
    for i in range(len(B)):
        if B[i] != A[idx+i]:
            isSub=False
            break
else:
    isSub = False

if isSub:
    print('Yes')
else:
    print('No')