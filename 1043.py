def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

import sys
input = sys.stdin.read
data = input().strip().split("\n")

N, M = map(int, data[0].split())
known_info = list(map(int, data[1].split()))
kn = known_info[0]
if kn > 0:
    known_people = known_info[1:]
else:
    known_people = []

parties = []
for i in range(2, 2 + M):
    party_info = list(map(int, data[i].split()))
    parties.append(party_info[1:])

# Initialize Union-Find
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

# Union known people
for person in known_people:
    union(parent, rank, known_people[0], person)

# Union people within the same party
for party in parties:
    for i in range(1, len(party)):
        union(parent, rank, party[0], party[i])

# Count the number of parties where you can lie
count = 0
truth_parent = find(parent, known_people[0]) if kn > 0 else None

for party in parties:
    can_lie = True
    for person in party:
        if kn > 0 and find(parent, person) == truth_parent:
            can_lie = False
            break
    if can_lie:
        count += 1

print(count)
