n, m = map(int, input().split())

dic = {}
ndic = {}
for i in range(n):
    s = input()
    dic[s] = i+1
    ndic[i+1] = s

for j in range(m):
    s = input()
    if s.isnumeric():
        print(ndic[int(s)])
    else:
        print(dic[s])