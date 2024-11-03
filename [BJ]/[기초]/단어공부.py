from collections import Counter

word = input().strip().upper() # 문자열 입력 받음 / upper() 대문자 변환
#소문자 변환

counter = Counter(word) # 알파벳 빈도 계산

most_common = counter.most_common(2) # most_common
print(most_common)

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print("?")
else:
    print(most_common[0][0])