def solution(phone_book):
    
    # 전화번호 정렬
    # sort 원본 자체를 정렬함
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        #현재 번호가 다음 번호의 접두어인지 확인
        #startswith 접두어 확인 메서드 <-> endswith 접미사 메서드
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True