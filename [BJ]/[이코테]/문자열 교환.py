def solution(s):
    
    # a의 개수를 계산하여 슬라이딩 윈도우의 크기로 사용함
    a_count = s.count('a')
    
    extend_s = s+s # 원형 연결
    
    #첫번째 윈도우에서 b의 개수를 세어 초기화
    b_count = sum(1 for i in range(a_count) if extend_s[i] == 'b')
    min_swap = b_count
    
    for i in range(a_count, len(extend_s)):
        if extend_s[i-a_count] == 'b':
            b_count -= 1
        if extend_s[i] == 'b':
            b_count += 1
        min_swap = min(min_swap, b_count)
        
    return min_swap
        


s = input().strip() # 문자열 받기
print(solution(s)) # 
