import sys
input = sys.stdin.readline
pizza = {'1/4':0, '1/2':0, '3/4':0}
for i in range(int(input())):
    pizza[input().strip()]+=1
    
sol = 0

sol+=pizza['1/2']//2
pizza['1/2']%=2

if pizza['1/2'] and pizza['1/4']>1:
    pizza['1/2']-=1
    pizza['1/4']-=2
    sol+=1

sol+=pizza['3/4']
if pizza['3/4']>=pizza['1/4']:
    pizza['3/4']=0
    pizza['1/4']=0
else:
    pizza['1/4']-=pizza['3/4']
    pizza['3/4']=0

sol+=pizza['1/4']//4
pizza['1/4']%=4

if (pizza['1/2'] and pizza['1/4']==1) or (pizza['1/4'] and not pizza['1/2']) or (pizza['1/2'] and not pizza['1/4']):
    sol+=1
    pizza['1/2']=pizza['1/4']=0

print(sol)