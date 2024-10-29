from collections import Counter

def solution(base_word, word):
    count1 = Counter(base_word)
    count2 = Counter(word)
    
    #문자열 길이 비교
    length_diff = abs(len(base_word)-len(word))

    if count1 == count2:
        return True
    
    if length_diff >1:
        return False
    
    diff = sum((count1-count2).values()) + sum((count2-count1).values())
    
    return diff <=2

n = int(input())
words = [input().strip() for _ in range(n)]

word0 = words[0]
similar_count = 0

for word in words[1:]:
    if solution(word0,word):
        similar_count +=1
        
print(similar_count)