n = int(input())
li = []
for i in range(n):
    day, dow,  weather = input().split()
    if weather == 'Rain':
        li.append((day, dow, weather))

li.sort(key = lambda x: x[0])

print(li[0][0], li[0][1], li[0][2])