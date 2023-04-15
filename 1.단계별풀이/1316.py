import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    word = input().strip()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            word1 = word[j+1:]
            if word[j] in word1:
                N -= 1
                break
print(N)