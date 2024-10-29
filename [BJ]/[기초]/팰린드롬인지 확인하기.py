word = input().strip()

#문자열 뒤집기
#word[::] 전체 리스트를 의미함
if word == word[::-1]:
    print(1)
    
else:
    print(0)