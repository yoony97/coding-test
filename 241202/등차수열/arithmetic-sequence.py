n = int(input())
nums = list(map(int, input().split()))

ans = 0
for k in range(100):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            ai = nums[i]
            aj = nums[j]
            if k - ai == aj - k:
                cnt  += 1
    ans =  max(cnt, ans)

print(ans)