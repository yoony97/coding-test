n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    min_idx = i
    for j in range(i, n):
        if a[min_idx] > a[j]:
            min_idx = j
    
    if min_idx != i:
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

print(' '.join([str(i) for i in a]))
