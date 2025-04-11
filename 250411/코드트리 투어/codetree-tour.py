import heapq
import sys
input = sys.stdin.readline

isMade = [False]*(30_001)
isCancel = [False]*(30_001)

def make_graph(cmd):
    N, M = cmd[1], cmd[2]
    graph = [[]*N for i in range(N)]
    raw_graphs = cmd[3:]
    for i in range(0, len(raw_graphs), 3):
        u,v,w= raw_graphs[i], raw_graphs[i+1], raw_graphs[i+2]
        graph[u].append((v, w)) # dest, weight
        graph[v].append((u, w))
    return N, M, graph

def dijkstra(start, graph, N):
    D = [float('inf')]*N
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
    
    return D


def addPackage(pid, revenue, dest, D, plan):
    isMade[pid] = True
    cost = D[dest]
    profit = revenue - cost
    heapq.heappush(plan, (-profit, pid, revenue, dest))
    
def cancelPackage(pid):
    isCancel[pid] = True

def sellPacakge(plan):
    while plan:
        if -1*plan[0][0] < 0: #이득을 못얻으면 그냥 -1만 출력함
            break
        p = heapq.heappop(plan)
        pid = p[1]
        if not isCancel[pid]: #취소되지 않은 것
            return pid
    return -1

def changeStart(new_start, plan, graph, N):
    D = dijkstra(new_start, graph, N)
    temp = []
    new_plan = []
    while plan:
        p = heapq.heappop(plan)
        temp.append(p)

    for i in temp:
        _, pid, revenue, dest = i
        addPackage(pid, revenue, dest, D, new_plan)

    return new_plan

def main():
    Q = int(input())
    D = []
    plan = []
    for i in range(Q):
        cmd = list(map(int, input().split()))
        command = cmd[0]
        if command == 100:
            N, M, graph = make_graph(cmd)
            D = dijkstra(0, graph, N)
        if command == 200:
            pid, revenue, dest = cmd[1:]
            addPackage(pid, revenue, dest, D, plan)
        if command == 300:
            cancelPackage(cmd[1])
        if command == 400:
            print(sellPacakge(plan))
        if command == 500:
            plan = changeStart(cmd[1], plan, graph, N)
            


main()