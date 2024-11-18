n, m = map(int, input().split())

answer = 0
for i in range(1,max(n,m)+1):
    if n%i == 0 and m%i == 0:
        answer = max(answer, i)

print(answer)