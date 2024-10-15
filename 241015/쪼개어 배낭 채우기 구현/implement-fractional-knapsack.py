N, M = map(int, input().split())

li = []
for i in range(N):
    w, v = map(int, input().split())
    ratio = v/w
    li.append((ratio, w))

li.sort(key =lambda x: x[0], reverse=True)


current_w = 0
value = 0

for ratio, weight in li:
    if current_w < M:
        #print(current_w, value)
        if current_w + weight <= M:
            current_w += weight
            value += (ratio*weight)
        else:
            res_weight = M - current_w
            current_w += res_weight
            value += (ratio*res_weight)

print(format(value, '.3f'))