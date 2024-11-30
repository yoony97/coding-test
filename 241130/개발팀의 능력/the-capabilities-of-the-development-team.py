# 2명 1명 뽑으면 2명 자동 뽑힘
li = list(map(int, input().split()))
total = sum(li)
ans = float('inf')
isfind = False
for i in range(5):
    for j in range(i+1, 5):
        for k in range(5):
            if k == i or k == j:
                continue
            
            A = li[i] + li[j]
            B = li[k]
            C = total - A - B
            
            if A != B and B != C and A != C:
                isfind = True
                maxT = max(A,B,C)
                minT = min(A,B,C)
                ans = min(ans, maxT- minT)
if isfind:
    print(ans)
else:
    print(-1)