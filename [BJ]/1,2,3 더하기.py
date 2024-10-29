T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    n = int(input()) # 정수 n
    
    if n <= 3:
        print([0,1,2,4][n]) # n이 1,2,3 d 인 경우 출력
        
    else:
        dp = [0] * (n+1) # 직관적으로 index 만들기 위해서
        dp[:4] = [0,1,2,4]
        
        #동적 계획법으로 dp[i] 계산
        for i in range(4,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        print(dp[n])
        
        