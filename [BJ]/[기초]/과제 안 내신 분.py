#1부터 30까지의 번호를 집합으로 생성
all_students = set(range(1,31))


for _ in range(28):
    submit_student = int(input().strip()) #제출한 학생
    all_students.remove(submit_student) # 제출한 학생 제외
    
# sorted -> 집합을 리스트로 변환함
missing_students = sorted(all_students) # 집합 sorted
print(missing_students[0])
print(missing_students[1])

