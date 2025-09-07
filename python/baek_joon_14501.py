# DP
import sys

n = int(sys.stdin.readline().rstrip())
# table 길이를 n+1로 함 (key)
table = [0 for _ in range(n+1)]
schedule = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# Concept
# 1일에 잡혀있는 상담(10만원)이 3일 걸림 -> 4일때 10만원 정산한다
# 만약 7일짜리 상담 스케줄이면, Table 은 길이가 8 이어야 한다 (n+1인 이유)
# (7일에 잡혀있는 상담이 1일 걸릴수도 있기 때문)

for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if table[j] < table[i] + schedule[i][1]:
            table[j] = table[i] + schedule[i][1]

print(max(table))
