
def solution(s):
    counter = 0

    for char in s:
        if char == '(':
            counter += 1
        else: #char == ')'
            counter -= 1
            if counter < 0:
                return False

    return counter == 0

print(solution("()()"))  # True
print(solution("(())()"))  # True
print(solution(")()("))  # False
print(solution("(()("))  # False