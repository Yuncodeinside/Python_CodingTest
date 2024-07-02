def solution(prices):
    n = len(prices) # 주식 가격의 길이
    answer = [0]*n  # 배열 초기화
    stack = [] # 인덱스 저장
    
    for i in range(n):
        # 현재 가격이 스택의 마지막 가격보다 낮을 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop() # 스택에서 인덱스를 꺼냄
            answer[j] = i-j # 남은 시간 계산
        #stack이 비어 
        stack.append(i)
    
    #스택에 남아 있는 인덱스
    while stack:
        j = stack.pop()
        answer[j] = n-1-j
        
    return answer


print(solution([1, 2, 3, 2, 3]))  # 결과: [4, 3, 1, 1, 0]