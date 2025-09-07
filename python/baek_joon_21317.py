import sys

n = int(sys.stdin.readline().strip())
stone = []

dp = [1e10]*n  # float('inf')
dp[0] = 0  # No energy

# Populate dp table using small and big jumps
for i in range(n-1):
    s, b = map(int, sys.stdin.readline().split())
    stone.append((s, b))
    if i+1<n: dp[i+1] = min(dp[i+1], dp[i]+s)  # Small jump
    if i+2<n: dp[i+2] = min(dp[i+2], dp[i]+b)  # Big jump

# Read the energy cost of the super big jump
k = int(sys.stdin.readline().strip())

# The minimum energy when the super big jump is not used
dp_without_super = dp[-1]

# The minimum energy when the super big jump is used once
dp_with_super = 1e10

# Try applying the super big jump at different positions
for i in range(n-3):
    new_dp = dp[:]  # Create a copy of the dp array
    new_dp[i+3] = min(new_dp[i+3], new_dp[i] + k)  # Apply super big jump

    # Recalculate dp values after the super big jump
    for j in range(i+3, n-1):
        if j+1<n: new_dp[j+1] = min(new_dp[j+1], new_dp[j] + stone[j][0])  # Small jump
        if j+2<n: new_dp[j+2] = min(new_dp[j+2], new_dp[j] + stone[j][1])  # Big jump

    # Update the minimum energy
    dp_with_super = min(dp_with_super, new_dp[-1])

# Print the minimum energy
print(min(dp_without_super, dp_with_super))
