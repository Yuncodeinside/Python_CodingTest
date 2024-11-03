import sys

input = sys.stdin.read()
data = input().splitlines() # 문자열을 줄바꿈을 기준으로 리스트로 반환
N = int(input()) # 좌표의 개수

point = [tuple(map(int,line.split())) for line in data[1:]]

point.sort()


