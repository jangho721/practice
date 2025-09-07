import sys

# Solution:
# Divide the ladder into two parts, above and below, based on row '?'

# Number of people
people = int(sys.stdin.readline().strip())

step = int(sys.stdin.readline().strip())

end = list(map(str, sys.stdin.readline().strip()))
start = sorted(end)

above_ladder = []
below_ladder = []

# Dividing the Ladder
for _ in range(step):
    row = list(map(str, sys.stdin.readline().strip()))
    if '?' in row:
        above_ladder = below_ladder
        below_ladder = []
        continue
    below_ladder.append(row)

# Top-down: start to ? row
for h in above_ladder:
    for idx, e in enumerate(h):
        if e == "-":
            start[idx], start[idx+1] = start[idx+1], start[idx]

# Bottom-up: end to ? row
for h in below_ladder[::-1]:
    for idx, e in enumerate(h):
        if e == "-":
            end[idx], end[idx+1] = end[idx+1], end[idx]

# Output
output = []
for ind in range(len(start)-1):
    if start[ind] != end[ind]:
        start[ind], start[ind + 1] = start[ind + 1], start[ind]
        output.append('-')
        continue
    output.append('*')

if start != end:
    output = ['x' for _ in range(people - 1)]
print("".join(output))
