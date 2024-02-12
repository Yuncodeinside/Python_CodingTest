def solution(ingredient):
    answer = 0 # 햄버거의 개수
    
    h = [] # 햄버거 재료 배열
    for i in ingredient:
        h.append(i) # 재료를 햄버거 배열에 추가
        #print(h)
        if h[-4:]==[1,2,3,1]:
            answer+=1
            #햄버거의 개수 추가
            for j in range(4):
                h.pop() #원소 4개 제외 0,1,2,3
                #print(h)
                
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))