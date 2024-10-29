def solution(n,computers):
    def dfs(computer):
        #현재 컴퓨터를 방문했음
        visited[computer] = True
        #현재 컴퓨터와 연결된 컴퓨터를 탐색함
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i) # 재귀함수
    
    visited = [False]*n #모든 컴퓨터가 처음에는 방문 되지 않음
    network_count = 0 #네트워크 개수를 저장할 변수
    
    for i in range(n):
        if not visited[i]: # 방문하지 않은 컴퓨터가 있으면
            dfs(i) # 그 컴퓨터와 연결된 모든 컴퓨터를 탐색
            network_count +=1 # 네트워크를 하나 발견했으므로 개수를 증가
            
            
    return network_count
            
    
    
