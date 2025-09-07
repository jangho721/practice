import sys

# Simulation
# Solution: You only need to consider how much water can be filled at the current position

n, m = map(int, sys.stdin.readline().strip().split())
block = list(map(int, sys.stdin.readline().strip().split()))

answer = 0

# Exclude the first and last blocks
for idx in range(1, m-1):
    # Find the maximum among the left blocks based on the current position
    left_block = max(block[:idx])
    # Find the maximum among the right blocks based on the current position
    right_block = max(block[idx+1:])

    temp = min(left_block, right_block)
    if temp > block[idx]:
        answer += temp - block[idx]

print(answer)
