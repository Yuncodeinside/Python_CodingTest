def solution(word):
    seen = set() # 이미 나온 단어 기록 집합
    prev_char = "" # 이전 문자 초기화
    
    for char in word:
        if char != prev_char:
            if char in seen: # 문자가 떨어져서 다시 등장하면 그룹 단어가 아님
                return False
            seen.add(char) # 새로운 문자 기록(이미 나온 단어 집합에 기록함)
            prev_char = char # 현재 문자를 이전 문자로 업데이트
    return True
            

N = int(input()) # 단어의 개수
count =0

for _ in range(N): # 단어 입력 받기
    word = input().strip()
    if solution(word): # 그룹 단어라면 개수 증가
        count +=1

print(count)
