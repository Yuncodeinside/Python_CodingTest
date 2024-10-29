from collections import deque

N = int(input())

cards = deque(range(1, N+1)) #1 ~ N 까지의 번호 생성 후 큐에 넣기

#남는 카드의 숫자가 1이 될 때까지 반복함
while len(cards) > 1:
    cards.popleft() # 맨 앞 원소(맨 위에 있는 카드)를 바닥에 버리고
    cards.append(cards.popleft()) #  제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮김
    
print(cards[0]) # 마지막에 남은 카드 출력