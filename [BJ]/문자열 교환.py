
def min_swap(s):
    
    n = len(s)
    a_count = s.count('a') # a의 개수
    extended_s = s+s #문자열 확장
    min_window = float('inf')
    
    b_count = 0
    
    #슬라이딩 윈도우를 사용하여 a_count 크기의 윈도우 내에서 b의 개수를 찾음
    for i in range(a_count):
        if extended_s[i] == 'b':
            b_count += 1
    min_window = b_count
    current_b_count = b_count # current b 초기화
    
    #슬라이딩 윈도우를 이동하면서 최소 b의 개수 찾기 
    for i in range(a_count, len(extended_s)):
        if extended_s[i-a_count] == 'b':
            current_b_count -= 1
        if extended_s[i] == 'b':
            current_b_count += 1
        min_window = min(min_window, current_b_count)
    
    return min_window

s = input().strip() # 입력받기
print(min_swap(s))