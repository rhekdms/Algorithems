import sys
input = sys.stdin.readline
X,A,B,C,D = map(int,input().split())
sol = [0,0,0,0]
for d in range(X//25,-1,-1):
    for c in range((X-d*25)//10,-1,-1):
        for b in range((X-d*25-c*10)//5,-1,-1):
            a = X-d*25-c*10-b*5
            check = [a,b,c,d]
            if a<=A and b<=B and c<=C and d<=D and sum(sol)<=sum(check):
                sol = check
print(*sol)