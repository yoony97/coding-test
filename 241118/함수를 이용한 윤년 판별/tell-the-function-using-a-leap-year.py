def is_magic(year):
    if year%400 != 0 and year%100 == 0:
        return True
    if year%4 == 0 and year%100 != 0:
        return True
    return False

n = int(input())

if is_magic(n):
    print('true')
else:
    print('false')