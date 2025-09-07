# DP
# Bottom-up
import sys

n = int(sys.stdin.readline().strip())
steps = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 캐싱
dp = [0] * n

# 첫번째 칸
dp[0] = steps[0]

# 두번째 칸
if n > 1:
    dp[1] = steps[0] + steps[1]

# 세번째 칸
# 첫번째 + 세번째 or 두번째 + 세번째
if n > 2:
    dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])

# 연속 3개를 밟을 수 없음
# Case1. 두 계단 전에서 현재로 바로 넘어오는 경우
# Case2. 세 계단 전에서 직전 계단을 밟고 넘어오는 경우
for i in range(3, n):
    dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])

print(dp[-1])
