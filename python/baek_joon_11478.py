import sys

S = sys.stdin.readline().strip()

result = set()

length = len(S)

for i in range(length):
    for j in range(i+1, length+1):
        result.add(S[i:j])

print(len(result))
