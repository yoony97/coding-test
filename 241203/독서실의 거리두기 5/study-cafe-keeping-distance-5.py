N = int(input())
arr = list(map(int, str(input())))
ans = 0 
for current in range(N):
    if arr[current] == 1:    
        isfind = False
        for nxt in range(current+1, N):
            if arr[nxt] == 1:
                isfind = True
                break
        if isfind:
            ans = max((nxt-current)//2, ans) 
        else:
            ans = max(N-current -1, ans)

print(ans)

        
                

        