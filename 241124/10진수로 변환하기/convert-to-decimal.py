n = [int(s) for s in input()]
c = 1
ans = 0
for i in n[::-1]:
    ans += i*c
    c *= 2

print(ans)