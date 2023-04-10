import sys
input = sys.stdin.readline
hour, minute = map(int,input().split())
time = int(input())
minute += time
while minute >= 60:
    minute -= 60
    hour += 1
    if hour > 23:
        hour = 0
print(hour, minute)
'''
시간 분 0~23 0~59
요리시간

끝나는 시간

요리시간이 60 이상이면 분+요리시간이 60 미만이 될 때 까지 -60 , - 할때마다 시간+1
시간이 23 초과하면 0부터 시작
'''