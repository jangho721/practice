import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
row, col, d = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# 청소 X: 0, 청소 O: -1

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean = 0

while True:
    check = 0

    #현재 위치 청소
    if matrix[row][col] == 0:
        # 청소하면 -1
        matrix[row][col] = -1
        clean += 1

    # 주변 4칸 중 청소 여부 확인
    for i, j in zip(dx, dy):
        if matrix[row+i][col+j] == 0:
            check += 1
            break

    # 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if check == 0:
        dxx = -dx[d]
        dyy = -dy[d]
        if matrix[row+dxx][col+dyy] == 1:
            break
        row = row+dxx
        col = col+dyy
        continue

    # 청소되지 않은 빈 칸이 있는 경우
    else:
        d -= 1
        if d < 0:
            d += 4
        while True:
            dxx = dx[d]
            dyy = dy[d]
            if matrix[row+dxx][col+dyy] == 0:
                row = row + dxx
                col = col + dyy
                break
            else:
                d -= 1

print(clean)
