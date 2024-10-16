n = int(input())
s = set()
for i in range(n):
    op, num = input().split()
    num = int(num)
    if op == 'add':
        s.add(num)
    elif op == 'remove':
        s.remove(num)
    elif op == 'find':
        print(str(num in s).lower())