def solution(money):
    #아메리카노의 잔수
    cup = money//5500
    #거스름돈
    change = money%5500
    answer = [cup,change]
    
    return answer