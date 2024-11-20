_ = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def isSame(A,B):
    if B[0] in A:
        idx = A.index(B[0])
        if len(A[idx:]) < len(B):
            return "No"
        for i in range(len(B)):
            if A[idx+i] != B[i]:
                return "No"
        return "Yes"
    else:
        return "No"


print(isSame(A,B))
