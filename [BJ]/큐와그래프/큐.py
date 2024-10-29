from collections import deque
import sys

input = sys.stdin.read
queue=deque()

def process_commands(commands):
    result = []
    
    for command in commands:
        if command.startswith("push"):
            _, X = command.split() # push "10"
            queue.append(int(X))
            
        elif command == "pop":
            if queue:
                result.append(queue.popleft()) # 큐에서 가장 앞의 원소를 꺼냄.
            else: # 큐에 정수가 없는 경우
                result.append(-1)
        elif command == "size":
            result.append(len(queue))
            
        elif command == "empty":
            result.append(1 if not queue else 0) # 큐가 비어 있으면 1 아니면 0을 출력함
        
        elif command == "front":
            if queue: # 큐에 정수가 들어 있는 경우
                result.append(queue[0])
            else:
                result.append(-1)
        elif command == "back":
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)
                
    return result

if __name__ == "__main__":
    data = input().splitlines() # 입력된 데이터를 줄 단위로 분리하여 리스트로 반환함
    N = int(data[0]) # 명령어의 개수
    commands = data[1:N+1] # 이후 명령어
    
    results = process_commands(commands)
    sys.stdout.write("\n".join(map(str,results))+"\n")
    