def solution(prices):
    n = len(prices)
    #리스트 초기화
    answer = [0]*n
    stack = []
    
    for i in range(n):
        
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = n-1-j
        
    return answer


print(solution([1, 2, 3, 2, 3]))  # 결과: [4, 3, 1, 1, 0]