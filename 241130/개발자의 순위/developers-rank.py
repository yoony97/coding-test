K, N = map(int, input().split())
li = []
for i in range(K):
    li.append(list(map(int, input().split())))

# li: a b c d > 1등 a, 2등 b , ... 라는 의미
# 항상 a번 개발자가 b번 개발자보다 더 높은 순위였던 서로 다른 (a,b) 쌍 수 구하기
results = set([])
for i in range(K):
    result = set([])
    for j in range(N):
        for k in range(j+1, N):
            result.add((li[i][j],li[i][k]))

    if not results:
        results = results.union(result)
    else:
        results = results.intersection(result)

print(len(results))