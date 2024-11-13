n = int(input())
five = n//5
n = n%5
if n%2 == 0:
    print(five + n//2)
else:
    print(-1)
