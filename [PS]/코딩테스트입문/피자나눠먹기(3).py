def solution(slice, n):
    
    # 필요한 총 조각 수를 피자 조각 수로 나눔
    # 나머지가 있으면 나누기전에 추가되도록
    answer = (n + slice -1)//slice
    
    return answer