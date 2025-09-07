import sys

def possible_path(line):
    """
    1. 차이가 1만 경사로 설치 가능
    2. 현재 높이 < 이전 높이, 경사로 설치를 위해 오른쪽 스캔
    3. 현재 높이 > 이전 높이, 경사로 설치를 위해 왼쪽 스캔
       (낮은 곳에 경사로 설치)
    """

    for j in range(1, n):
        # 차이가 1만 가능
        if abs(line[j] - line[j - 1]) > 1:
            return False

        # 현재 < 이전, 경사로를 만들기 위해 오른쪽 스캔
        if line[j] - line[j - 1] == -1:
            # l 만큼 경사로 너비 필요
            for k in range(l):
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                if j + k >= n or used[j + k] or line[j] != line[j + k]:
                    return False

                # 높이가 같은 경우 사용 여부 체크
                if line[j] == line[j + k]:
                    used[j + k] = True

        # 현재 > 이전, 경사로를 만들기 위해 왼쪽 스캔
        elif line[j] - line[j - 1] == 1:
            # l 만큼 경사로 너비 필요
            for k in range(l):
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                if j - k - 1 < 0 or line[j - 1] != line[j - k - 1] or used[j - k - 1]:
                    return False

                # 높이가 같은 경우 사용 여부 체크
                if line[j - 1] == line[j - k - 1]:
                    used[j - k - 1] = True

    # 모두 문제없이 설치된 경우 가능함을 출력
    return True


n, l = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

path = 0

# 가로
for i in range(n):
    # 경사로 사용 여부 저장
    used = [False for _ in range(n)]
    # 현재 확인할 길을 입력
    if possible_path(map[i]):
        path += 1

# 세로
for i in range(n):
    # 경사로 사용 여부 저장
    used = [False for _ in range(n)]
    # 현재 확인할 길을 입력
    if possible_path([map[j][i] for j in range(n)]):
        path += 1

print(path)
