n, k  = map(int, input().split())
li = list(map(int, input().split()))

max_val = 0
for i in range(n-k+1):
    val =  0
    for j in range(i, i+k):
        val += li[j]
    max_val = max(max_val, val)

print(max_val)