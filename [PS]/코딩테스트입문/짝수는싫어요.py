def solution(n):
    # // 몫
    # / 나누기
    # % 나머지
    return [x for x in range(n+1) if x % 2]
# x % 2 == 1 는 True 이면 나머지가 1인 홀수들만 뽑게됨
