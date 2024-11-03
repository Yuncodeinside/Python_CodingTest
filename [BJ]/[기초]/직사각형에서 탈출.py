x,y,w,h = map(int,input().split())

#네 가지 거리계산(직사각형의 경계선)
left = x
right = w-x
bottom = y
top = h-y

min_distance = min(left,right,bottom,top)
print(min_distance)
