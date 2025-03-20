n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
i = 0 
answer = True
for j in range(m):
    while i < n and A[i] != B[j]:
        i+=1
    if i >= n:
        answer= False
        break


if answer:
    print("Yes")
else:
    print('No')
