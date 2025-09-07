import sys

count = int(sys.stdin.readline()) # 스위치 개수
state = list(map(int, sys.stdin.readline().split())) # 스위치 상태
n = int(sys.stdin.readline()) # 학생 수
switch = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 성별, 스위치 번호

# checking
if count != len(state):
    exit()

for person in switch:
    # rule (1) : Man
    if person[0] == 1:
        i = 1
        while i*person[1] <= len(state):
            if state[i*person[1]-1] == 1:
                state[i*person[1]-1] = 0
            else:
                state[i*person[1]-1] = 1
            i += 1

    # rule (2) : Woman
    elif person[0] == 2:
        i = 0
        index = person[1]-1

        while index-i >= 0 and index+i <= count-1 and (state[index-i] == state[index+i]):
            if state[index-i] == 0:
                state[index-i] = 1
                state[index+i] = 1
            else:
                state[index-i] = 0
                state[index+i] = 0
            i += 1

for i in range(1, count+1):
    print(int(state[i - 1]), end=" ")
    if i % 20 == 0:
        print("")
