n = int(input())

def temp(n, last):
    for i in range(1,n+1):
        num = last+1
        if num == 10:
            num = 1
        print(num, end=' ')
        last = num
    print()
    return num

last = 0
for i in range(n):
    last = temp(n, last)