
numbers = input().strip() # 숫자를 문자열로 입력받기

sorted_digits = sorted(numbers,reverse=True) # 내림차순 정렬

print("".join(sorted_digits))# 리스트를 문자열로 합쳐서 출력함
