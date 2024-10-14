n, m = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
maximum = max(max(li1),max(li2))
num2count = { i : 0 for i in range(1, maximum+1)}

for i, num in enumerate(li1):
    num2count[num] += 1 

s = ''
for j in li2:
    s += str(num2count[j]) +' '

print(s.strip())