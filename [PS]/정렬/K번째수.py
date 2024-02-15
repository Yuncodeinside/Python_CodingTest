def solution(array,commands):
    result = []
    for command in commands:
        i,j,k = command
        #i번째부터 j번째까지 자르고 정렬함(리스트 인덱스가 0부터 시작하므로 i-1부터 j)
        sliced_arr = sorted(array[i-1:j])
        
        #k번째 숫자 출력
        result.append(sliced_arr[k-1])
        # arr.inser(index,value) 를 이용하면 특정 인덱스에 요소 추가
        
    return result
        
        
        