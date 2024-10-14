n, k = map(int, input().split())
li = list(map(int, input().split()))
dic = {} # dict[i-k] += 1
cnt = 0

for i in range(n):
    a = k-li[i]
    if a not in dic:
        dic[a] = 0
    dic[a] += 1

answer = 0
for i in range(n):
    if li[i] in dic:
        answer += dic[li[i]]//2

print(answer)