import sys
import time
input = sys.stdin.readline

A,B,C = map(int,input().split())
def f(a,n):
  if n == 1:
      return a%C
  else:
      tmp = f(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % C
      else:
          return (tmp  * tmp *a) %C
          
print(f(A,B))