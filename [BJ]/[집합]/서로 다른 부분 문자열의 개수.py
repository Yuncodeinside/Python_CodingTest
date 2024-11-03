
s = input().strip() # 문자열 입력

# 집합 - 중복 방지
sub_string_set = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub_s = s[i:j]
        sub_string_set.add(sub_s)
        print("i and j",i,j)
        print("sub_s",sub_s)
        print(sub_string_set)

print(len(sub_string_set))