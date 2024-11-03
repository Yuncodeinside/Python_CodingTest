
def solution(S):
    position=[-1]*26
    
    for idx, char in enumerate(S):
        pos = ord(char) - ord('a')
        
        if position[pos] == -1:
            position[pos] = idx # 인덱스
    print(" ".join(map(str,position)))

S = input().strip()
solution(S)