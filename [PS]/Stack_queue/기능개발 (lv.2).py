from collections import deque

def solution(progresses, speeds): #작업 진도 및 작업 속도 배열을 받음
    days= []
    answer = []
    
    Speeds = 0 # 개발 속도
    
    for i in range(0, len(progresses)):
        # ceil 반올림 메서드
        days.append(math.ceil((100-progresses[i])/speeds))
    
    
    
    
    
    return answer