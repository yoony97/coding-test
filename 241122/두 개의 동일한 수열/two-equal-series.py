n = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = True
for i, j in zip(A,B):
    if i != j:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")