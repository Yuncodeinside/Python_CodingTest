def solution(emergency):
    
    #응급도와 인덱스를 쌍으로 묶어 리스트를 만듬
    indexed_emergency = list(enumerate(emergency))
    #print("",indexed_emergency)
    
    # 응급도를 기준으로 내림차순 정렬 (70,60,40,..)
    sorted_emergency = sorted(indexed_emergency, key=lambda x: x[1], reverse=True)
    #print(sorted_emergency)
    
    #1차원 리스트를 초기화
    order = [0] * len(emergency)
    #print(order)
    
    #정렬된 리스트를 순회하면서 각 요소의 원래 인덱스 위치에 순위를 매김
    #rank , index, emergency
    for rank, (index,_) in enumerate(sorted_emergency,start=1):
        #rank 를 1부터 시작한다는 의미임
        order[index] = rank
    return order

print(solution([3, 76, 24]))  # 결과: [3, 1, 2]
print(solution([1, 2, 3, 4, 5]))  # 결과: [5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100]))  # 결과: [2, 4, 3, 5, 1]