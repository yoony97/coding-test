n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

#u의 끝이 d의 앞으로 가고
#d의 끝이 u의 앞으로 간다.

for i in range(t):
    u_end = u[-1]
    d_end = d[-1]
    
    #무브 해라
    for i in range(n-1, -1, -1):
        u[i] = u[i-1]
        d[i] = d[i-1]
    u[0] = d_end
    d[0] = u_end


print(' '.join([str(i) for i in u]))
print(' '.join([str(i) for i in d]))
    
