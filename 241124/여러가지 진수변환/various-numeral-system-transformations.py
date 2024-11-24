n, b = map(int, input().split())
li = []

while True:
    if n < b:
        li.append(n)
        break
    else:
        li.append(n%b)
        n = n//b

for i in li[::-1]:
    print(i, end='')