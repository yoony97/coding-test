n = int(input())
numbers = [int(input()) for _ in range(n)]
psum = [0]*(n+1)

for i in range(n):
    psum[i+1] = psum[i] + numbers[i]

L = 0 
R = n-1
max_range = 0
max_sum = 0
for L in range(n):
    for R in range(L+1, n):
        s = psum[R] - psum[L-1]
        if max_sum < s and s%7 == 0:
            max_sum = s
            max_range = max(max_range, R-L+1) 


print(max_range)