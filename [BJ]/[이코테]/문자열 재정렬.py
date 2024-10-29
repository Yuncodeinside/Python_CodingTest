N = input()

letters = [] # 문자열 
sum_of_digits = 0 # 숫자

for char in N:
    if char.isdigit(): # 숫자인지 확인함
        sum_of_digits += int(char)
    else: # 문자인 경우
        letters.append(char)
        
# 문자 오름차순 정렬
letters.sort()

#join 함수를 통해 문자열 삽입함
result = ''.join(letters)

# 숫자가 있다면 숫자도 붙여서 출력함
if sum_of_digits > 0:
    result += str(sum_of_digits)

print(result)
