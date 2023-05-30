V = int(input())
score = input()
if score.count('A') > V//2:
    print('A')
elif score.count('B') > V//2:
    print('B')
else:
    print('Tie')