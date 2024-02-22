def solution(price):
    
    #price의 범위 및 10원 단위
    if 10 <= price <=1000000 and price % 10 == 0:
        #큰 값부터 적어야함
        # 50만원 이상이므로 >=
        if price >= 500000:
            discount = 0.20

        elif price >= 300000:
            discount = 0.10

        elif price >= 100000:
            discount = 0.05

        else:
            discount = 0.00
            
        #정수 리턴
        answer = int(price * (1-discount))
    
    return answer