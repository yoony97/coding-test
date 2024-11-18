a, b = map(int, input().split())


def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

answer = 0

for i in range(a, b+1)
    if is_prime(i):
        answer+= i
print(answer)