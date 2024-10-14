n, m = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

num2count ={}

for i, num in enumerate(li1):
    if num not in num2count:
        num2count[num] = 0
    num2count[num] += 1 

s = ''
for j in li2:
    if j not in num2count:
        s += '0 '
    else:
        s += str(num2count[j]) +' '

print(s.strip())