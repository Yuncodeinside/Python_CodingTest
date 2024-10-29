from collections import deque

def solution(bridge_length, weight, truck_weight):
    bridge = deque([0]* bridge_length) # 다리 위 상태 (큐)
    current_weight = 0 # 다리 위에 있는 트럭들의 현재 무게
    time = 0 # 경과 시간
    index = 0 # 대기 중인 트럭 인텍스
    
    while bridge:
        time += 1 # 시간
        current_weight -= bridge.popleft() # 다리의 맨 앞 트럭이 나가면 무게에서 제외함
        
        if index < len(truck_weight):
            #트럭이 버티고 있는 무게 내에서 트럭을 올릴 수 있는지 확인 후 괜찮으면 통과
            if current_weight + truck_weight[index] <= weight:
                bridge.append(truck_weight[index])  # 트럭 다리에 올리기
                current_weight += truck_weight[index] # 현제 무게 증가
                index += 1 # 대기 중인 다음 트럭으로 이동
            else:
                bridge.append(0)
                
    return time
    