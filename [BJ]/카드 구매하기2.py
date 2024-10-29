N = int(input()) #카드의 개수
P = [0] + list(map(int, input().split())) # 카드팩 가격 저장

dp = [float('inf')] * (N+1)
dp[0] = 0 # 0개의 카드를 사는 비용은 0

for i in range(1, N+1):
    for j in range(1,i+1): # 카드를 i개 살 때, j개의 카드가 들어 있는 카드팩을 사용함
        dp[i] = min(dp[i], dp[i-j]+ P[j]) # 동적 계획법을 이용해 최소 비용을 계산함
    
print(dp[N])