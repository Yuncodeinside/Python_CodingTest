
numbers = [int(input()) for _ in range(5)]

average = sum(numbers) //5

#중앙값
numbers.sort()
median = numbers[2]

print(average)
print(median)