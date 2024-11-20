a , b = map(int, input().split())

if a < b:
    a += 10
    b = b*2
else:
    b += 10
    a = a*2

print(a,b)