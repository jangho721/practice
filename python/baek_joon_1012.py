# DFS, BFS
# deque library (BFS)
import sys
sys.setrecursionlimit(10000)
from collections import deque

# The number of problems
n = int(sys.stdin.readline().strip())

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if (0 <= mx < col) and (0 <= my < row):
            if field[mx][my] == 1:

                # 방문 처리
                field[mx][my] = 0
                dfs(mx, my)

for _ in range(n):
    # Total land, Land planted with cabbage
    col, row, point = map(int, sys.stdin.readline().strip().split())

    # The list inside represents the columns.
    # Therefore, the number of elements must be as many as the number of rows.
    field = [[0 for _ in range(row)] for _ in range(col)]

    # Minimum number of white worm
    count = 0

    # Cabbage location
    for _ in range(point):
        x, y = map(int, sys.stdin.readline().strip().split())

        # Cabbage
        field[x][y] = 1

    # Search for all points
    for i in range(col):
        for j in range(row):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
