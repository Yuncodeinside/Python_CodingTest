def solution(S):
    #알파벳 배열 생성
    position = [-1]*26
    
    #
    for idx , char in enumerate(S):
        pos = ord(char) - ord('a')
        #print(pos, ord(char) , ord('a'))
        
        # 알파벳의 위치가 기록되지 않았다면, 
        if position[pos] == -1:
            position[pos] = idx
    
    print(" ".join(map(str, position)))

S = input().strip()
solution(S)