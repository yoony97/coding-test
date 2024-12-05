a, b, c = list(map(int, input().split()))

dist1 = abs(a-b)
dist2 = abs(b-c)

count = 0
if dist1 == 0 and dist2 == 0:
    count = -1
elif dist1 == 1 and dist2 == 1:
    count = 0
elif dist1 <= 2 and dist2 <= 2:
    count = 1
else:
    count = max(dist1, dist2) - 1
print(count)
