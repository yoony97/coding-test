N = int(input())
li = list(map(int, input().split()))

start = 0
end = 0
sums = sum(li[start:end])
for i in range(1,N):
    if sums + li[i] > li[i]:
        end = i
    else:
        start = i

print(sum(li[start:end]))