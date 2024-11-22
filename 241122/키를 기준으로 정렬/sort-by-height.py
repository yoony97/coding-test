n = int(input())
li = []
for i in range(n):
    name, height, weight = input().split()
    li.append((name, int(height), int(weight)))
    
li.sort(key = lambda x: x[1])

for (name, height, weight) in li:
    print(name, height, weight)