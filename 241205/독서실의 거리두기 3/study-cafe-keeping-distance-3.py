N = int(input())
st = list(map(str, input()))
max_dist = 0

def min_dist():
    min_dis = float('inf')
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if st[i] == st[j] == '1':
                dist = abs(j-i)
                min_dis = min(dist, min_dis)
    return min_dis

for i in range(N):
    if st[i] == '0':
        st[i] = '1' #새로 투입한 인원
        m = min_dist()
        #print(''.join(st), m)
        max_dist = max(m, max_dist)
        st[i] ='0'

print(max_dist)