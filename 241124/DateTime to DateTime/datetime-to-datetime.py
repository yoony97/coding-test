a, b, c = map(int, input().split())
cd = 11
ch = 11
cm = 11
count = 0

while True:
    if cd == a and ch == b and cm == c:
        break

    if  cm == 60:
        cm = 0
        ch += 1
    
    if ch == 24:
        ch = 0
        cd +=1
    cm += 1
    count += 1

print(count)