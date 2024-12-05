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
for i in range(N):
    if i >= P-1:
        reader.add(messages[i][0])


if messages[P-1][1] != 0:
    print(' '.join(people - reader))


#읽었다
# - 읽기만하고, 메세지를 안보낸 경우
# - 메세지를 보낸 경우,
