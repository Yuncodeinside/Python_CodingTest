from collections import Counter

def count_permutations(g, s_len, W, S):
    # W와 S의 빈도 카운트를 저장
    w_counter = Counter(W)
    s_counter = Counter(S[:g])
    print(w_counter)
    print(s_counter)
    
    count = 0
    # 초기 윈도우가 W의 순열인 경우
    if s_counter == w_counter:
        count += 1

    # 슬라이딩 윈도우로 이동하면서 카운트를 비교
    for i in range(g, s_len):
        print("iiiiiiiiii",i," ",i-g)
        start_char = S[i - g]  # 윈도우의 시작 문자
        print("sssssssssss",start_char)
        end_char = S[i]        # 윈도우의 끝 문자
        print("eeeeeeeeeee",end_char)
        
        s_counter[end_char] += 1
        if s_counter[start_char] == 1:
            del s_counter[start_char]
        else:
            s_counter[start_char] -= 1
        
        # 윈도우가 W의 순열인지 확인
        if s_counter == w_counter:
            count += 1
    
    return count

# 입력 받기
g, s_len = map(int, input().split())
W = input().strip()
S = input().strip()

# 결과 출력
print(count_permutations(g, s_len, W, S))
