from collections import deque
import sys

#목적: 입력받은 도로 정보를 바탕으로 그래프를 구성하고
#출발 도시로부터 BFS를 수행하여 각 도시까지의 최단거리를 구함

def find_cities():

    # 입력 N 도시의 개수 M 단방향 도로의 개수 K 최단 거리 X 출발도시
    #N,M,K,X = map(int, input().split())
    N,M,K,X = map(int, sys.stdin.readline().split())


    # 도시 간의 연결 정보를 저장하기 위한 그래프
    graph = [[] for _ in range (N+1)] # 0 ~ N 도시

    # 단방향으로 이어진 도시들을 그래프에 저장
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b) # a->b

    #distance 배열은 각 도시까지의 최단 거리를 기록함
    distance = [-1] * (N+1) # 처음에는 모든 도시를 -1로 초기화
    distance[X] = 0 # 출발 도시 X는 자기 자신이므로 0으로 설정

    queue = deque([X]) #BFS 수행
    #print(queue)

    while queue:
        city = queue.popleft() # 큐에서 도시를 꺼내서
        #print(queue)
        
        for next_city in graph[city]: # 해당 도시에서 갈 수 있는 도시 확인
            if distance[next_city] == -1: # 방문하지 않은 도시인 경우
                distance[next_city] = distance[city] + 1
                queue.append(next_city)
                
    found = False
    for i in range(1,N+1):
        if distance[i] == K:  # 최단 거리가 k인 도시 출력
            print(i)
            found = True

    #도시가 없는 경우
    if not found:
        print(-1)
    
            
find_cities()
