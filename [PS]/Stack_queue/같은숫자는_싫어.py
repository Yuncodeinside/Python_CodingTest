def solution(arr):
    answer = []
    
    #음수를 우선 할당하여 첫번째 요소가 무조건 추가되도록 함
    last =-1
    
    for a in arr:
        #이전 값과 같지 않을 때만 a를 추가함
        if a != last:
            answer.append(a)
            #다음 비교를 위해 값을 last 에 넣어줌
        last=a
    
    return answer


print(solution([1,1,2,3,1]))