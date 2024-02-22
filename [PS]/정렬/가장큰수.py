def solution(numbers):
    
    #각 숫자를 문자열로 변환 후 str()
    # map 객체를 -> list 로 변환함
    numbers = list(map(str, numbers))
    print(numbers)
    
    #비교를 위해 문자열을 3번 반복하고 내림차순으로 정렬함
    #정렬된 수를 이어 붙여서 가장 큰 수를 만들어 반환함
    #list.sort() : 원본 자체를 정렬
    #sorted() : 원본 변형하지 않고 새로운 리스트 반환
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers.sort(key=lambda x: x*3, reverse=True))
    
    lam1 = lambda x: x*3
    print("lamda",lam1(numbers))
    print(".",numbers)
    
    #결과값을 정수로 변환 후 다시 문자열로 변환함
    answer = str(int(''.join(numbers)))
    print(answer)
    
    return answer

print(solution([6,10,2]))