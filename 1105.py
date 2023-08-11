import sys
L,R = sys.stdin.readline().split()
if '8' not in L or '8' not in R:
	print(0)
elif L == R:
    print(L.count('8'))
else:
	L = L.zfill(len(R))
	print(min(L[0:len(L)-len(str(int(R)-int(L)))].count('8'),R[:len(R)-len(str(int(R)-int(L)))].count('8')))
 
'''
더 짧고 빠른 코드
L, R = input().split()
ans = 0
if len(L) == len(R):
    for v1, v2 in zip(L, R):
        if v1 != v2:
            break
        if v1 == '8':
            ans += 1

print(ans)
'''