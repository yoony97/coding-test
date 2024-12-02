N = int(input())
seq = input()#list(map(str, input()))
ans = float('inf')
for length in range(1,N+1):
    prev = 0
    fali = False
    li = []
    for i in range(N+1):
        s = seq[i:i+length]
        if s not in li:
            li.append(s)
        else:
            fali = True
            break
        #prev = target

    if not fali:
        #print(li)
        print(length)
        break

    