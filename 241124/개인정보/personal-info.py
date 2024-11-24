li = []
for _ in range(5):
    name, height, weight = input().split()
    li.append((name, int(height), float(weight)))

li.sort(key=lambda x: x[0])
print('name')
for i in li:
    print(" ".join([str(s) for s in i]))
print()
li.sort(key=lambda x: (-x[1]))
print('height')
for i in li:
    print(" ".join([str(s) for s in i]))
