n = int(input())
li = list(map(int, input().split()))
a = []
ans = dict()

for idx, i in enumerate(li, start=1):
    a.append((i, idx))

a.sort(key= lambda x: x[0])

for idx, i in enumerate(a, start=1):
    ans[i[1]] = idx

for i in range(1,n+1):
    print(ans[i], end = " ")



#어디로 스왑이 되었는가?를 확인할려면 어떤 방법이 있을까?
# d[3] = 1 -> 4로 변경된걸 어떻게 알아?



