def is_magic(year):
    if year%100 != 0:
        if year%4 == 0:
            return True
        else:
            return False
    else:
        if year >=400 and year%400 != 0:
            return True
        else:
            return False


    
n = int(input())

if is_magic(n):
    print('true')
else:
    print('false')