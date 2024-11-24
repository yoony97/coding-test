n = int(input())
li = []

if n == 0:
    li.append(n)

while n > 0:
    li.append(n%2)
    n = n//2

print(''.join([str(s) for s in li[::-1]]))