# BFS
import sys
from collections import deque

# Input
m, n, h = map(int, sys.stdin.readline().strip().split())

# Create a box
# h, n, m (Index)
box = []
box_append = box.append

for _ in range(h):
    temp_box = []
    temp_append = temp_box.append
    for __ in range(n):
        temp_append(list(map(int, sys.stdin.readline().strip().split())))
    box_append(temp_box)

# The direction of movement
dm = [0, 0, 1, -1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dh = [1, -1, 0, 0, 0, 0]

queue = deque()

# Ripe tomatoes
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))


while queue:

    # Number of tomatoes to be checked at the same time
    length = len(queue)
    for _ in range(length):
        h_, n_, m_ = queue.popleft()

        # 6 directional checking
        for idx in range(6):
            m_s = m_ + dm[idx]
            n_s = n_ + dn[idx]
            h_s = h_ + dh[idx]

            # (Conditions) In a box, unripe tomatoes
            if (0 <= m_s < m) and (0 <= n_s < n) and (0 <= h_s < h):
                if box[h_s][n_s][m_s] == 0:
                    box[h_s][n_s][m_s] = box[h_][n_][m_] + 1

                    queue.append((h_s, n_s, m_s))

# Checking
days = 0
for layer in box:
    for row in layer:
        for element in row:
            # If you have unripe tomatoes
            if element == 0:
                print(-1)
                exit(0)

        days = max(days, max(row))

# You have to do -1 because you started with day 1 in the beginning
print(days - 1)
