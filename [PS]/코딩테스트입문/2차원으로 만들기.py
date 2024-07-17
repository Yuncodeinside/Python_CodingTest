def solution(num_list,n):
    
    #결과를 저장할 리스트
    result = []
    
    for i in range(0,len(num_list),n):
        result.append(num_list[i:i+n])
        
    return result


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(solution(num_list, n))  # 출력: [[1, 2], [3, 4], [5, 6], [7, 8]]