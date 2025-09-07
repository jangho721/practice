board = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]

count = 0

def checking(L):

    num = 0

    for i in range(5):
        if sum(L[i]) == 0:
            num += 1

    for i in range(5):
        count_temp = 0
        for j in range(5):
            if L[j][i] == 0:
                count_temp += 1
        if count_temp == 5:
            num += 1

    left_up = []
    right_down = []
    for i in range(5):
        left_up.append(L[i][i])
        right_down.append(L[i][4 - i])

    if sum(left_up) == 0:
        num += 1
    if sum(right_down) == 0:
        num += 1

    return num

for bingo_row in range(5):
    for bingo_col in range(5):
        for board_row in range(5):
            for board_col in range(5):
                if bingo[bingo_row][bingo_col] == board[board_row][board_col]:
                    board[board_row][board_col] = 0
                    count += 1
                if count >= 12: # 3개의 빙고를 맞출 수 있는 최소의 count 수.
                    if checking(board) >= 3:
                        print(count)
                        exit()
