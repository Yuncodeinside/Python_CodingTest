N , K = map(int, input().split())
score = list(map(int, input().split()))

# 내림차순 정렬
score.sort(reverse=True)
print(score[K-1])