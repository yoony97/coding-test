m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nod = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = 0
if m1 <= m2:
    for i in range(m1, m2):
        days += num_of_days[i]

    days = days - d1
    days = days + d2
else:
    for i in range(m2, m1):
        days += num_of_days[i]
    days = days - d2
    days = days + d1

print(nod[days%7])


