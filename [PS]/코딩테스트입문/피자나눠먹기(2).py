import math

def solution(n):
    i=1
    while(i):
        #6*i 피자의 총 조각
        #n으로 나눈 나머지가 0이 될때 i 를 반환함
        if (6*i)%n == 0:
            return i
        i+=1
    return i

def solution2(m):
    print((n*6))
    #gcd() 최대 공약수 함수
    print(math.gcd)