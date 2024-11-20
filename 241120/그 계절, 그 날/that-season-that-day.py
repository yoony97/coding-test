# 4 6 9 11 = 30  else 31 
y, m, d = tuple(map(int, input().split()))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def exist_month30(m, d):
    if d <=28:
        return True
    else:
        return False  

def exist_month31(m, d, leaf):
	
    if m == 2:
        if leaf:
            if d > 29:
                return False
            else:
                return True
        else:
            if d > 28:
                return False
            else:
                return True
    if d <= 31:
        return True
    else:
        return False

ans = False
leaf = is_leap_year(y)

if m == 4 or m == 6 or m ==  9 or m == 11:
    ans = exist_month30(m,d)
else:
    ans = exist_month31(m,d, leaf)

if ans:
    if 3 <= m <= 5:
        print('Spring')
    elif 6<= m <=8:
        print('Summer')
    elif 9<= m <=11:
        print('Fall')
    else:
        print('Winter')


else:
    print(-1)
