import sys

test_case = int(sys.stdin.readline())

def rotation(n, d, arr):

    max_count = int(360/45) # 최대 회전 가능 횟수
    rot_count = int(abs(d)//45)

    if d < 0:
        rot_count = max_count - rot_count

    for i in range(rot_count):
        temp_list = []

        for _ in range(n): # 주 대각선 -> 가운데 열
            temp = arr[_][(n//2)]
            arr[_][(n//2)] = arr[_][_]
            temp_list.append(temp)

        for _ in range(n): # 가운데 열 -> 부 대각선
            temp = temp_list[_]
            temp_list[_] = arr[_][n-1-_]
            arr[_][n-1-_] = temp

        for _ in range(n): # 부 대각선 -> 가운대 행
            temp = temp_list[_]
            temp_list[_] = arr[(n//2)][n-1-_]
            arr[(n//2)][n-1-_] = temp

        for _ in range(n): # 가운대 행 -> 주 대각선
            arr[_][_] = temp_list[n-1-_]

for i in range(test_case):
    n, d = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    rotation(n, d, arr)

    for j in range(n):
        for k in range(n):
            print(arr[j][k], end=' ')
        print()
