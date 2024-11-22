class P:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

a,b,c = input().split()
p = P(a,b,c)

print('secret code :',p.a)
print('meeting point :',p.b)
print('time :',p.c)

