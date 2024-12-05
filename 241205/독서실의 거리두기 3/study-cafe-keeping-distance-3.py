def dist(A,B):
    return B-A

N = int(input())
st = input()
max_dist = 0
for i in range(N):
    
    for j in range(i+1,N):
        if st[i] =='1' and st[j] == '1':
            dis = dist(i,j)
            max_dist = max(max_dist, dis//2)
            break

print(max_dist)