# 주어진 동전들이 전부 배수관계에 놓여있기 때문입니다
# 배수 관계에 놓여있는 동전이 주어졌을 때에는, 항상 큰 동전부터 이용하는 것이 좋음을 알 수 있습니다.

N, K = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

ans = 0
for i in reversed(li):
    K = K - i*(K//i)
    ans += K//i

print(ans)