m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cm = m1
cd = d1
count = 1
while True:    
    count += 1
    if cd == num_of_days[cm]:
        cm += 1
        cd = 1
    else:
        cd += 1
    

    if cm == m2 and cd == d2:
        break

print(count)

