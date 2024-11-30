li = list(map(int, input().split()))
sums = sum(li)
max_s = float('inf')
for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == j or  j== k or i==k: #같은 선수는 안뽑아야해
                continue
            else:
                #print(i,j,k, s)
                a = li[i]  +  li[j] + li[k]
                b = sums - a
                #print(i,j,k, s)
                max_s = min(max_s, abs(a-b))

print(max_s)