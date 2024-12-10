n = int(input())
li = list(map(int, input().split()))

sort = False
while not sort:
    sort = True
    for i in range(1,n):
        if li[i] < li[i-1]:
            temp = li[i]
            li[i] = li[i-1]
            li[i-1] = temp
            sort = False

print(' '.join([str(i) for i in li]))