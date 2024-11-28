def iscarry(A,B,C):
    for a, b, c in zip(A,B,C):
        a, b, c = int(a), int(b), int(c)
        if a+b+c >= 10:
            return False
    return True




N = int(input())
numbers = []
for i in range(N):
    num = input()
    if len(num) < 5:
        num = '0'*(5-len(num)) + num
    numbers.append(num)
ans = -1
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if iscarry(numbers[i], numbers[j], numbers[k]):
                a, b, c = int(numbers[i]), int(numbers[j]), int(numbers[k])
                ans = max(a+b+c, ans)
    
print(ans)