a, b = map(int, input().split())

def is_magic(num):
    if '3' in str(num) or '6' in str(num) or '9' in str(num) or num%3 == 0:
        return True
    return False

answer = 0
for i in range(a,b+1):
    if is_magic(i):
        answer+=1

print(answer)