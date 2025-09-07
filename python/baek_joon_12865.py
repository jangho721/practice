import sys

n, m = map(int, sys.stdin.readline().strip().split())

item_weight = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    item_weight.append((w, v))

dp = [0 for i in range(m+1)]

for weight, value in item_weight:
    for idx in range(m, weight-1, -1):
        dp[idx] = max(dp[idx], dp[idx-weight]+value)

print(dp[-1])

# Knapsack problem
# 2차원 배열 사용 방법
n, m = map(int, input().split())

things = [[0, 0]]
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    things.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][m])
