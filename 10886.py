N = int(input())
cute = []
for i in range(N):
    cute += [int(input())]
if cute.count(1)>N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")