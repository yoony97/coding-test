N, M, P  = map(int, input().split())
TOTAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
people = set(map(str, TOTAL[:N]))
messages = []
reader = set()
for i in range(M):
    c, u = input().split()
    u = int(u)
    messages.append((c, u))

#확실하게 읽은 사람
prev_c, prev_u = messages[0]
if P-1 == 0:
    reader.add(prev_c)
for i in range(1,N):
    c, u = messages[i]
    if i >= P-1:
        reader.add(c)
    if prev_u == u:
        reader.add(prev_c)
    prev_c, prev_u = c, u

#번호로 비교하기





if messages[P-1][1] != 0:
    print(' '.join(people - reader))


