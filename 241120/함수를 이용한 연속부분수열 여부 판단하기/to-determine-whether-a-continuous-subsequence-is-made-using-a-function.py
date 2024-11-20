_ = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
idx = A.index(B[0])
isSub = True
for i in range(len(B)):
    if B[i] != A[idx+i]:
        isSub=False
        break


if isSub:
    print('Yes')
else:
    print('No')