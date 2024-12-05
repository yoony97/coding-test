n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

temp = 0
ans = 0
for i in range(n):
    people = (A[i] +  temp) - B[i]
    ans +=  people
    temp = people


print(ans)