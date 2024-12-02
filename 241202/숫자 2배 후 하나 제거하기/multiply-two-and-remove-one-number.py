n = int(input())
numbers = list(map(int, input().split()))
ans = float('inf')
for i in range(n): # 두배가 될 숫자 위치 i
    numbers[i] *= 2
    for j in range(n): #제거할 숫자 j
        remains = []
        for k in range(n):
            if j == k:
                continue
            remains.append(numbers[k])
        sum_diff = 0
        for l in range(n-2):
            sum_diff += abs(remains[l] - remains[l+1])
        #print(remains, sum_diff)
        ans = min(sum_diff, ans)
    
    numbers[i] //= 2

print(ans)

