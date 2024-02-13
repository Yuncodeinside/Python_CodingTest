
def solution(priorities,location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    print("queue",queue)
    #리스트에 우선순위와 인덱스를 튜플로 묶어 저장함
    
    answer = 0
    #특정 작업이 몇번째로 저장되는지 저장하는 변수
    
    #무한 루프
    while True:
        #가장 먼저 시작 되는 작업을 빼서 cur에 저장함
        #실행 대기 큐에서 대기 중인 프로세스를 하나 꺼냄
        cur = queue.pop(0)
        print("cur",cur)
        
        # 큐에 대기 중인 프로세스 중 우선 순위가 더 높은 프로세스가 있다면
        # 하나라도 q[1]가 더 크다면
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            #프로세스를 실행함
            print("queue",queue)
        
        #만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행함    
        else:
            #현재 작업이 큐 안에 있는 다른 작업보다 우선순위가 높으면
            answer += 1
            print("answer",answer)
            # location은 대기 큐에 있는 프로세스 - 1
            if cur[0] == location:
                print("cur[0]:",cur)
                print("answer",answer)
                return answer
            
# location : 몇번째로 실행되는지 알고 싶은 프로세스의 위치 
print(solution([2,1,3,2],2))
            