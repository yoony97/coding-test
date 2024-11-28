N = int(input())
people = []

for i in range(N):
    people.append(int(input()))

ans = float("inf")
#[4, 7, 8, 6, 4]
for start in range(N):
    current = start
    dis = 0
    for c in range(N):
        dis += people[current]*c
        #print(start, current, people[current], dis)
        current = (current + 1)%N
        
    ans = min(dis, ans)
print(ans)