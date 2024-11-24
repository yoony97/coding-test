n = int(input())
li = []
for _ in range(n):
    name, s1, s2, s3 = input().split()
    li.append((name, int(s1), int(s2), int(s3)))

li.sort(key=lambda x: x[1] + x[2] + x[3])
for i in li:
    print(' '.join([str(s) for s in i]))