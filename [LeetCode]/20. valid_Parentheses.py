#유효한 괄호

def isValid(s):
    stack = []
    table = {')':'(','}':'{',']':'['}

    for char in s:
        if char not in table:
            # dict table에 key로 존재하지 않는다면 stack에 추가함 (),],})
            stack.append(char)
        #여는 괄호 key와 일치하지 않으면 false를 반환함 
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

#print(isValid("()[]{}"))
print(isValid("][()}{"))



 
