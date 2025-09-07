import sys

col, row = map(int, sys.stdin.readline().split())
count = int(sys.stdin.readline())
store_location = [list(map(int, sys.stdin.readline().split())) for _ in range(count)]
start = list(map(int, sys.stdin.readline().split()))

# 1 : North, 2 : South, 3 : West, 4 : East
total = 0
for i, j in store_location:
    if i == start[0]: # 위치가 같은 경우
        total += abs(j-start[1])
    else: # 위치가 다를 경우
        if (i <= 2 and start[0] <= 2) or (i > 2 and start[0] > 2): # 서로 마주보고 있는 방향일 경우
            if i <= 2:
                total += row
                temp_1 = start[1] + j
                temp_2 = (col-start[1]) + (col-j)
                if temp_1 < temp_2:
                    total += temp_1
                else:
                    total += temp_2
            else:
                total += col
                temp_1 = start[1] + j
                temp_2 = (row-start[1]) + (row-j)
                if temp_1 < temp_2:
                    total += temp_1
                else:
                    total += temp_2
        else: # 마주보고 있는 방향 외 : 8 가지의 경우
            if i == 1: # North
                if start[0] == 3: # West
                    temp = j + start[1]
                    total += temp
                else: # East
                    temp = col - j + start[1]
                    total += temp
            elif i == 2: # South
                if start[0] == 3: # West
                    temp = row - j + start[1]
                    total += temp
                else: # East
                    temp = (col - j) + (row-start[1])
                    total += temp
            elif i == 3: # West
                if start[0] == 1:  # North
                    temp = j + start[1]
                    total += temp
                else:  # South
                    temp = row - j + start[1]
                    total += temp
            elif i == 4: # East
                if start[0] == 1:  # North
                    temp = col - j + start[1]
                    total += temp
                else:  # South
                    temp = (col - j) + (row-start[1])
                    total += temp

print(total)
