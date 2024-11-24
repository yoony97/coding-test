m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nod = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
current = 0
cnt = 0
target = input()
target_idx = nod.index(target)

while True:
    if m1 == m2 and d1 == d2:
        break


    if num_of_days[m1] == d1:
        m1 += 1
        d1 = 1
    else:
        d1 += 1

    current = (current+1)%7
    
    if target_idx == current:
        cnt += 1

print(cnt)