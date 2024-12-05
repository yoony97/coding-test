N = int(input())
st = list(map(int, input()))

prev = 0
candidate = (0, N)
max_dist = 0
for i in range(1,N):
    if st[i] == 1:
        if max_dist < (i - prev):
            candidate = (prev, i)
            max_dist = i - prev 
        prev = i

st[(candidate[0]+candidate[1])//2] = 1
prev = 0
max_dist = float('inf')
for i in range(1,N):
    if st[i] == 1:
        dist = i - prev
        max_dist = min(max_dist, dist)
        prev = i
#print(st)    
print(max_dist)
    