def solution(array):
    
    #리스트 오름차순 정렬
    array.sort()
    # // 몫 연산자
    mid_idx = len(array)//2
    
    return array[mid_idx]