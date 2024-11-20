m, op, n = input().split()
m, n = int(m), int(n)

if op =='+':
    answer = m+n
    print(f"{m} {op} {n} = {answer}")

elif op =='-':
    answer = m-n
    print(f"{m} {op} {n} = {answer}")

elif op =='*':
    answer = m*n
    print(f"{m} {op} {n} = {answer}")

elif op =='/':
    answer = m//n
    print(f"{m} {op} {n} = {answer}")

else:
    print('False')