# DFS: 재귀, BFS: while
import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())

# making box
# empty box
box = [[] for _ in range(col)]

# Fill an empty box
for _ in range(row):
    temp = list(map(int, sys.stdin.readline().split()))
    for idx, i in enumerate(temp):
        box[idx].append(i)

queue = deque()
# Append the ripe tomatoes to the queue
for x in range(col):
    for y in range(row):
        if box[x][y] == 1:
            queue.append((x,y))

# BFS
# Up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# Repeat until there are no more ripe tomatoes
while queue:
    # Repeat for the number of ripe tomatoes currently in the queue
    length = len(queue)
    for _ in range(length):
        # Take one ripe tomato out of the queue
        x, y = queue.popleft()

        # Compare the adjacent tomatoes of the ripe tomato
        for i in range(4):
            x_s = x + dx[i]
            y_s = y + dy[i]

            # Unless it goes out of the bounds of the tomato grid
            if (0 <= x_s < col) and (0 <= y_s < row):
                # Only if the tomato is unripe
                if box[x_s][y_s] == 0:
                    # Since it started at 1, you need to subtract 1 at the end
                    box[x_s][y_s] = box[x][y] + 1
                    # Since it is now a ripe tomato, insert it into the queue
                    queue.append((x_s, y_s))

# check
day = 0
for x_axis in box:
    for element in x_axis:
        
        # If there are still unripe tomatoes after running BFS
        if element == 0:
            # If it's impossible for all tomatoes to ripen, return -1
            print(-1)

            # exit(1): Forced termination due to an error
            # Normal termination
            exit(0)

    # Find the maximum value among the tomatoes
    day = max(day, max(x_axis))

# Since the ripe tomatoes (1) were incremented by 1, the final result should be -1
print(day - 1)
