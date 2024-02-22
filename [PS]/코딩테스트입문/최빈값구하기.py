def solution(array):
    count = {} #딕셔너리 생성
    for i in array:
        if i not in count:
            #처음 나온 수
            count[i] = 1
        else:
            # 빈도수 추가
            count[i] += 1
            
            #내림차순 저장
            # items() 딕셔너리 키,값 쌍을 얻음
            #sorted() Tuple pair로 이루어진 list를 리턴함
    sorted_count = sorted(count.items(), key=lambda item : item[1], reverse = True)
    #print("1",sorted_count)
    #print("2",len(sorted_count))
    
    #최빈값이 여러개일 때
    if len(sorted_count) > 1 and sorted_count[0][1] == sorted_count[1][1]:
        #이차원 배열?
        
        return -1
            
    return sorted_count[0][0]

a = [2,3,4,2]
print(solution(a))