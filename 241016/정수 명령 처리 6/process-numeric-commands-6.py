import heapq
class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, e):
        heapq.heappush(self.items, -e)
    
    def empty(self):
        if not self.items:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            return -1
        else:
            return -heapq.heappop(self.items)
        
    def top(self):
        if self.empty():
            return -1
            
        return -self.items[0]

a = PriorityQueue()

n = int(input())
for i in range(n):
    op = input().split()
    if op[0] == 'push':
        a.push(int(op[1]))
    elif op[0] == 'size':
        print(a.size())
    elif op[0] == 'empty':
        print(a.empty())
    elif op[0] == 'pop':
        print(a.pop())