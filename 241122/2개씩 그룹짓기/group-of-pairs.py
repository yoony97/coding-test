n = int(input())
li = list(map(int, input().split()))
ans = []
li.sort()
for i in range(n):
    ans.append(li[i] + li[2*n-1-i])

#print(ans)
print(max(ans))


#2, 3, 5, 5
