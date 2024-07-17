def solution(numbers, direction):
    if direction == "right":
        #대괄호[] -> numbers[-1]/numbers[0]은 리스트가 아니기 때문 
        return [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        return numbers[1:] + [numbers[0]]
    else:
        raise ValueError("direction must be either 'left' or 'right'")

# 예제 사용
numbers = [1, 2, 3, 4, 5]
direction_right = "right"
direction_left = "left"
print(solution(numbers, direction_right))  # 출력: [5, 1, 2, 3, 4]
print(solution(numbers, direction_left))   # 출력: [2, 3, 4, 5, 1]