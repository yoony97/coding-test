import heapq
import sys
input = sys.stdin.readline

isMade = [False] * 30001
isCancel = [False] * 30001
D = []  # ✅ 전역 D 선언
graph = []  # ✅ 그래프도 전역으로 설정 (changeStart에서도 사용)
N = 0

def make_graph(cmd):
    global graph, N
    N, M = cmd[1], cmd[2]
    graph = [[] for _ in range(N)]
    raw_graphs = cmd[3:]
    for i in range(0, len(raw_graphs), 3):
        u, v, w = raw_graphs[i], raw_graphs[i+1], raw_graphs[i+2]
        graph[u].append((v, w))
        graph[v].append((u, w))

def dijkstra(start):
    global D
    D = [float('inf')] * N
    D[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if D[curr_node] < curr_dist:
            continue
        for next_node, weight in graph[curr_node]:
            next_dist = curr_dist + weight
            if next_dist < D[next_node]:
                D[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

def addPackage(pid, revenue, dest, plan):
    isMade[pid] = True
    cost = D[dest]  # ✅ 전역 D 사용
    profit = revenue - cost
    heapq.heappush(plan, (-profit, pid, revenue, dest))

def cancelPackage(pid):
    if isMade[pid]:
        isCancel[pid] = True

def sellPackage(plan):
    while plan:
        if -plan[0][0] < 0:
            break
        p = heapq.heappop(plan)
        pid = p[1]
        if not isCancel[pid]:
            return pid
    return -1

def changeStart(new_start, plan):
    global D
    dijkstra(new_start)
    temp = []
    new_plan = []

    while plan:
        p = heapq.heappop(plan)
        temp.append(p)

    for i in temp:
        _, pid, revenue, dest = i
        if not isCancel[pid]:
            cost = D[dest]
            profit = revenue - cost
            new_plan.append((-profit, pid, revenue, dest))

    heapq.heapify(new_plan)
    return new_plan

def main():
    Q = int(input())
    plan = []
    for _ in range(Q):
        cmd = list(map(int, input().split()))
        command = cmd[0]

        if command == 100:
            make_graph(cmd)
            dijkstra(0)
        elif command == 200:
            pid, revenue, dest = cmd[1:]
            addPackage(pid, revenue, dest, plan)
        elif command == 300:
            cancelPackage(cmd[1])
        elif command == 400:
            print(sellPackage(plan))
        elif command == 500:
            plan = changeStart(cmd[1], plan)

main()