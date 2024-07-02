def solution(n):
    
    #변수를 0으로 초기화
    count = 0
    
    # 1~n까지 모든 숫자만큼 반복 
    for a in range(1,n+1):
        # 나머지 0 -> 자연수 숫자쌍이라는 것이므로 count 증가
        if n % a == 0:
            count += 1
    return count


print(solution(6))
print(solution(25))
print(solution(1))