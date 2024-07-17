def solution(numbers,k):
    # 공을 던질 때마다 인덱스가 2씩 증가함
    # % 나머지 반환
    index = (2*(k-1)) % len(numbers)
    return numbers[index]

numbers = [1, 2, 3, 4, 5]
K = 3
print(solution(numbers, K))  # 출력: 5

numbers = [1, 2, 3, 4, 5, 6]
K = 5
print(solution(numbers, K))  # 출력: 3