from collections import deque

#메모리 초과

#자료 구조 큐를 이용한 문제
def soulution(N,K):
    queue = deque(range(1, N+1))
    print("<",end="")
    
    while len(queue)>1:
        queue.rotate(-(K-1)) # K번째 사람을 앞으로 이동함
        print(queue.popleft(), end=', ')
        
    print(queue.popleft(),end='>')

N, K = map(int,input().split())
result = soulution(N,K)