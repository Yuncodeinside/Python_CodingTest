from itertools import combinations

# 카드의 개수, 수의 총 합
N , M =  map(int,input().split()) 
cards = list(map(int, input().split()))

cards_sum = 0
#조합 
for combo in combinations(cards,3):
    total = sum(combo)
    # M을 넘지 않으면서 sum보다 큰 경우에 업데이트
    if total <= M and total > cards_sum:
        cards_sum= total

print(cards_sum)

