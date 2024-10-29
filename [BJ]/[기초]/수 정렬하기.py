N = int(input())
numbers = [int(input()) for _ in range(N)]

# 오름차순 정렬
numbers.sort()

for number in numbers:
    print(number)