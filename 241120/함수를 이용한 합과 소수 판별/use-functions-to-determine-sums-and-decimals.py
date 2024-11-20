a, b = map(int, input().split())
def isprime(num):
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True

answer = 0
for i in range(a,b+1):
    if isprime(i):
        #print(i)
        if sum([int(s) for s in str(i)])%2 == 0:
            answer+=1

print(answer)
