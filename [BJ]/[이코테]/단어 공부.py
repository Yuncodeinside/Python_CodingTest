from collections import Counter

def most_frequent_letter(word):
    # 대소문자 구분 없애기
    word = word.upper()
    
    # 알파벳 빈도 계산
    counter = Counter(word)
    
    # 가장 많이 사용된 알파벳과 빈도 찾기
    most_common = counter.most_common()
    max_count = most_common[0][1] # 횟수
    print(most_common)
    print(max_count)
    
    # 최빈값이 여러 개 있는지 확인
    if len([count for letter, count in most_common if count == max_count]) > 1:
        return "?"
    else:
        return most_common[0][0]

# 입력 받기
word = input().strip()
print(most_frequent_letter(word))