def solution(age):
    
    #숫자를 문자열로 변환
    age_str = str(age)
    
    #각 숫자를 대응하는 알파벳으로 변환함
    #.join() -> 문자열 하나로 합침
    # int(char) -> 각 문자를 정수로 변환
    # for char in age_str:
    #     print(char,"--")
        
        #ord('a')는 문자 a의 유니코드 값을 반환함 -> 97
        #chr(ord('a')) + int(char)) 계산된 유니코드 값을 문자로 변환함
    age_alpha = ''.join(chr(ord('a')+ int(char)) for char in age_str)
    
    return age_alpha

print(solution(23))  # 결과: cd
print(solution(51))  # 결과: fb
print(solution(0))   # 결과: a
print(solution(89))  # 결과: ij