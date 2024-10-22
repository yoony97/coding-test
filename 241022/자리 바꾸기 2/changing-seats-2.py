import sys

#i분에 a1<->b1 자리 변경
#k분 동안 k번 자리 바꾸기
#K+1 ... 2*K 분동안 똑같이 벼녕
data = sys.stdin.read().strip().split("\n")

N, K = map(int, data[0].split())
change = [list(map(int, i.split())) for i in data[1:]]
count = [0]*(N+1)
s = [set() for _ in range(N+1)]

arr = [i for i in range(N+1)]

for i in range(1, N+1):
    s[i].add(i)
    count[i] = 1

for _ in range(3):
    for (a, b) in change:
        #print(arr, s, count)
        arr[a], arr[b] = arr[b], arr[a]

        if a not in s[arr[a]]:
            s[arr[a]].add(a)
            count[arr[a]] += 1
        
        if b not in s[arr[b]]:
            s[arr[b]].add(b)
            count[arr[b]] += 1

for i in range(1, N+1):
    print(count[i])