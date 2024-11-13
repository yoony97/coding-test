n = int(input())
li = list(map(int, input().split()))
buy = li[0]
answer = 0
for i in range(1, n):
    if buy > li[i]:
        buy = li[i]
    answer = max(li[i]- buy, answer)
    
print(answer)