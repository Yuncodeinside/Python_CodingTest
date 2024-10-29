heights = [int(input()) for _ in range (9)] # 일곱 난쟁이 입력 받기

total_sum = sum(heights) # 아홉 난쟁이 총합


#두 명을 제외하여 합이 100이 되는 일곱 난쟁이 찾기
found = False
for i in range(9):
    for j in range(i+1,9):
        if total_sum -heights[i] -heights[j] == 100:
            seven = [heights[k] for k in range(9) if k != i and k !=j] # 일곱 난쟁이 리스트
            found=True
            break
    
    if found:
        break
    
seven.sort()
#일곱 난쟁이 키 출력
for height in seven:
    print(height)