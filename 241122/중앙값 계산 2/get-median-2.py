n = int(input())
li = list(map(int, input().split()))
for i in range(n):
    if (i+1)%2 == 1:
        a = sorted(li[:i+1])
        #print(a, i//2)
        print(a[i//2], end=' ')
    