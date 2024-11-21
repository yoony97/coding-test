def print2(n):
    if n == 0:
        return   
    print2(n-1)
    print("HelloWorld")

n = int(input())
print2(n)
