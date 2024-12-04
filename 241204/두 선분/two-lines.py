x1, x2, x3, x4 = map(int, input().split())

if x2 < x3 and x4 < x1:
    print("intersecting")
else:
    print("nonintersecting")