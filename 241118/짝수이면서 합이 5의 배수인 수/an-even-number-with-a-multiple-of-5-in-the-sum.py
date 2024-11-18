n = input()

def is_magic(n):
    if int(n)%2 == 0 and (int(n[0]) + int(n[1]))%5 == 0:
        return True
    return False

if is_magic(n):
    print("Yes")
else:
    print("No")