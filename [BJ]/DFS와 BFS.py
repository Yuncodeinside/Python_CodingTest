from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v,end='')
    
    for neighbor in sorted(graph[v]): # 현재 정점 v에서 갈 수 있는 인접 정점들을 오름차순 정렬 , 항상 작은 번호의 정점을 먼저 방문
        if not visited[neighbor]: # 아직 방문하지 않은 정점을 체크
            dfs(graph,neighbor,visited) #재귀적으로 호출
            

#start : 탐색을 시작하는 정점
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft() # 큐의 가장 앞에 있는 정점을 꺼내기 위한 작업임
        print(v,end='')
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

N , M , V = map(int, input().split()) # 노드 개수, 간선 개수, 탐색 시작할 노드 번호
graph = {i:[] for i in range(1, N+1)} # 그래프 초기화 / 딕셔너리 형태
# {1: [] }

for _ in range(M): # 간선이 연결하는 두 정점(노드)의 번호
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 양방향 간선 처리

visited = [False] * (N+1) # 방문 여부 확인을 위해 사용 / 정점 번호와 일치시키기 위해 인덱스 0은 사용하지 않음
dfs(graph, V, visited)
print() # 줄바꿈
