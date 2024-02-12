import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()
    
    def push(self,x):
        self.q.append(x)
        
        #마지막에 삽입한 요소를 맨 앞에 두는 상태로 정렬함
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
    
    
m = MyStack()
print(m.push(1))
print(m.push(-1))
print(m.q)