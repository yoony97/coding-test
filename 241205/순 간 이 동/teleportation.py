A, B, x, y = map(int, input().split())
#순간이동 가능
#x -> y
#y -> x
#걷는 거리 최소화 하자
#가능한 경우의 수
# A -> B (순간 이동 안할 경우)
# A - > x -> y -> B (x로 간 담에 순간이동)
# A - > y -> x -> B (y로 간 담에 순간이동)

dist1 = abs(B-A)
dist2 = abs(x-A) + abs(B-y)
dist3 = abs(y-A) +  abs(B-x)
print(min(dist1,dist2,dist3))