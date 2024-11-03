import sys
input = sys.stdin.read

data = input().splitlines()
N = int(data[0]) # 좌표의 개수
point = [tuple(map(int, line.split())) for line in data[1:]] # 좌표 받기

#x좌표를 우선, x좌표가 같으면 y좌표 기준으로 정렬
point.sort()

for x,y in point:
    print(x,y)
