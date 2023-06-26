import sys
input=sys.stdin.readline

n,f=map(int,input().split())
l=list(map(int,input().split()))

s=l[0]
left=0
right=0

mx=float('inf')
cnt=1
while left<=right:
    if s==f:
        mx=min(mx,cnt)
    
    if s<f and right+1<n:
        right+=1
        s+=l[right]
        cnt+=1
    else:
        s-=l[left]
        left+=1
        cnt-=1

print(mx if mx!=float('inf')else 0)