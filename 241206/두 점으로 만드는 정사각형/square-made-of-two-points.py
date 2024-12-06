inputs1 = list(map(int, input().split()))
inputs2 = list(map(int, input().split()))

x1 = min(inputs1[0], inputs2[0])
y1 = min(inputs1[1], inputs2[1])
x2 = max(inputs1[2], inputs2[2])
y2 = max(inputs1[3], inputs2[3])

line = max((x2-x1),(y2-y1))

print(line*line)