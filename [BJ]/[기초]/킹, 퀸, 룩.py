correct_pieces = [1,1,2,2,2,8]
#입력 받기
pieces = list(map(int, input().split()))

result = [correct - found for correct , found in zip(correct_pieces,pieces)]
print(" ".join(map(str,result)))
# .join(list)