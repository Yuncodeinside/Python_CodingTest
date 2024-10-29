A,B = input().split() # 상근이가 칠판에 적은 두 수 a,b

A_reverse = int(A[::-1])
B_reverse = int(B[::-1])

if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)