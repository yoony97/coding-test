n = input()
li = list(map(int, input().split()))

def f(li):
    for i in range(len(li)):
        li[i] = abs(li[i])
    

f(li)
print(' '.join([str(i) for i in li]))