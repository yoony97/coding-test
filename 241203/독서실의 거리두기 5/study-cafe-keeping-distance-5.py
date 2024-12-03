N = int(input())
arr = list(map(int, str(input())))
ans = 0
idx = 0
min_dist = float('inf')
for current in range(N):
    if arr[current] == 1:    
        isfind = False 
        for nxt in range(current+1, N):
            if arr[nxt] == 1:
                isfind = True
                break
        if isfind:
            if ans < (nxt-current)//2:
                idx = nxt
                ans = max((nxt-current)//2, ans) 

        else:
            if ans < N-current - 1:
                ans = max(N-current -1, ans)
                idx = N-1

arr[idx] = 1

for current in range(N):
    if arr[current] == 1:    
        for nxt in range(current+1, N):
            if arr[nxt] == 1:
                min_dist = min(nxt-current-1, min_dist)
                break

print(min_dist)
