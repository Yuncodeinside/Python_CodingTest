def solution(prices):
    
    n = len(prices)
    answer = [0]*n #  결과 저장 배열
    stack = [] # 인덱스 저장 스택
    
    # 0~n-1
    for i in range(n):
        #스택이 비어있지 않고 현재 가격이 스택에 저장된 가격보다 작은 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j # 가격이 떨어지지 않은 기간을 계산함
            
        #스택이 비어 있는 경우 - 현재 인덱스를 스택에 추가함
        stack.append(i)
        
    #스택에 남아 있는 값은 끝까지 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1 # 끝까지 가격이 유지된 기간 계산
        
    return answer