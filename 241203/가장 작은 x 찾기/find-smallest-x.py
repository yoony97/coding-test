N = int(input())
li = []
MAX_NUM = 0
for i in range(N):
    a, b = map(int, input().split())
    li.append((a,b))
    MAX_NUM = max(MAX_NUM,a,b)


for num in range(1,MAX_NUM):
    current = num
    fail = False
    for i in range(N):
        current *= 2
        if not (li[i][0] <= current <= li[i][1]):
            #print(li[i][0], current, li[i][1])
            fail = True
            break
        
    if not fail:
        print(num)
        break


