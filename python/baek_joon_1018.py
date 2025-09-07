import sys

# m×n size board
# m, n = map(int, input().split())
m, n = map(int, sys.stdin.readline().split())

# Board
Board = []
append = Board.append
for _ in range(m):
    append(sys.stdin.readline().strip())

# Cut to size 8X8
count = []
for row in range(m - 7):  # 행
    for col in range(n - 7):  # 열
        """
            The beginning is white: start_w
            The beginning is black: start_b
        """
        start_w = 0
        start_b = 0
        for i in range(row, row+8):
            for j in range(col, col+8):
                """
                    It has one consistent color
                    when the sum of row and column indexes is even or odd.
                """
                if (i+j) % 2 == 0:
                    # The first element(0,0) is white.
                    if Board[i][j] == "W":
                        start_w += 1
                    # The first element(0,0) is black.
                    if Board[i][j] == "B":
                        start_b += 1
                else:
                    # The first element(0,0) is white.
                    if Board[i][j] == "B":
                        start_w += 1
                    # The first element(0,0) is black.
                    if Board[i][j] == "W":
                        start_b += 1

        count.append(start_w)
        count.append(start_b)

print(min(count))
