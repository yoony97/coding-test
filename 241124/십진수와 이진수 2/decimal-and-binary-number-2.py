N = [int(s) for s in input()]
ans = 0
c = 1
li = []

for i in N[::1]:
    ans += i*c
    c *= 2

ans = ans*17

while True:
    if ans < 1:
        li.append(ans)
        break
    else:
        li.append(ans%2)
        ans = ans//2

for i in li[::-1]:
    print(i, end="")
