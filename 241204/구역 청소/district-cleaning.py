a, b = map(int, input().split())
c, d = map(int, input().split())

ans = 0
if d < a or b < c: #안겹침
    ans = (b-a)+ (d-c)
else:
    s = min(a,b,c,d)
    e = max(a,b,c,d)
    ans = e-s

print(ans)