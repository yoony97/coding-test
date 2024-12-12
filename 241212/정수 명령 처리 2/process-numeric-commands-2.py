from collections import deque

class Queue:
    def __init__(self):          # 빈 큐 하나를 생성합니다.
        self.dq = deque()
                
    def push(self, item):        # 큐의 맨 뒤에 데이터를 추가합니다.
        self.dq.append(item)
                
    def empty(self):             # 큐가 비어있으면 True를 반환합니다.
        return not self.dq
                
    def size(self):              # 큐에 들어있는 데이터 수를 반환합니다.
        return len(self.dq)
        
    def pop(self):               # 큐의 맨 앞에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Queue is empty")
            
        return self.dq.popleft()
                
    def front(self):             # 큐의 맨 앞에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Queue is empty")
                        
        return self.dq[0]


n = int(input())
s = Queue()
for i in range(n):
    ops = input().split()
    if ops[0] ==  'push':
        s.push(int(ops[1]))
    if ops[0] ==  'size':
        print(s.size())
    if ops[0] ==  'empty':
        if s.empty():
            print(1)
        else:
            print(0)
    if ops[0] == 'pop':
        print(s.pop())
    if ops[0] == 'front':
        print(s.front())
