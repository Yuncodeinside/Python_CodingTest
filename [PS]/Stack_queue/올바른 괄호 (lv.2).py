
def solution(s):
    st = list() # 빈 리스트 생성
    for c in s:
        #여는 괄호일 때
        if c == '(':
            st.append(c)
            print(st)
        #닫는 괄호
        if c == ')':
            try:
                st.pop()
                print(st)
            except IndexError:
                return False

    return len(st) == 0

print(solution(")("))

