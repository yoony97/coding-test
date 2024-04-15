K, N = map(int, input().split(" "))
lens = []
for i in range(K):
    lens.append(int(input()))


L = 0
R = sum(lens)//N
max_length = 0
while L <= R:
    M = (L+R)//2
    cnt = 0
    
    if M == 0:
        M = 1

    for i in lens:
        cnt += i//M
    
    if cnt >= N:
        L = M + 1
        max_length = max(M, max_length)
    else:
        R = M - 1

print(max_length)