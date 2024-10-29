N = input()

length = len(N)

half = length//2

left_sum = sum(int(N[i]) for i in range(half))
right_sum = sum(int(N[i]) for i in range(half,length))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
    
