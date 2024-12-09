N = int(input())
li = list(map(int, input().split()))

for i in range(N):
    if (i+1)%2 == 1:
        temp = sorted(li[:i+1])
        print(temp[len(temp)//2], end =' ')
