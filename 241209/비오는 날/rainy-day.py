n = int(input())
D = []
for i in range(n):
    days, weekend, weather = input().split()
    year, month, day = days.split('-')
    if weather == 'Rain':
        D.append((year,month,day, f"{days} {weekend} {weather}"))

D.sort(key=lambda x : (x[0],x[1],x[2]))
print(D[0][-1])

