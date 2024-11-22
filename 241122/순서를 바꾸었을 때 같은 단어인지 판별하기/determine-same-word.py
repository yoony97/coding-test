a = [s for s in input()]
b = [s for s in input()]

a.sort()
b.sort()

a = ''.join(a)
b = ''.join(b)
if a == b:
    print('Yes')
else:
    print('No')