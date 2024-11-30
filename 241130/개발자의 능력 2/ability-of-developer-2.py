#3팀을 고르는거, 그럼 2팀을 고르면 확정
li = list(map(int, input().split()))
total=  sum(li)
L = len(li)
ans = float('inf')

for a in range(L):
    for b in range(L):
        if a != b:
            for i in range(L):
                if a != i and b != i:
                    for j in range(L):
                        if a != j and b != j and i != j:
                            A = li[a] + li[b]
                            B = li[i] + li[j]
                            C = total - A - B
                            maxT = max(A, B, C)
                            minT = min(A, B, C)
                            
                            if ans > maxT - minT:
                                ans = min(maxT-minT, ans)

print(ans)
