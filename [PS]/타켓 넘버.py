from collections import deque

def solution(numbers, target):
    queue = deque([(0,0)])
    count = 0
    
    while queue: # queue가 빌때까지 반복함
        
        #current_sum 은 현재까지의 합을 의미함 , idx는 numbers의 인덱스
        current_sum, idx = queue.popleft()
        print("idx",idx)
        print("len",len(numbers))
        if idx == len(numbers):
            #합과 target이 같다면 count 증가
            if current_sum == target:
                count += 1
            else:
                queue.append((current_sum + numbers[idx], idx+1))
                print(queue)
                queue.append((current_sum - numbers[idx], idx+1))
                print(queue)
                
        return count

print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))