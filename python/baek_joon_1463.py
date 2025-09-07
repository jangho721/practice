# DP
# Bottom Up (반복문-기본적으로) vs. Top Down (재귀)
import sys

# Default value: 1000 -> recursion limit을 조건에 맞게 풀어줘야 함
sys.setrecursionlimit(10000000)
number = int(sys.stdin.readline())

d = [0] * (number + 1)
# Top-Down 방식: 재귀 함수
def top_down(n):
    # base case: 1일 때 연산 횟수는 0
    if n == 1:
        return 0

    # 이미 계산된 값이 있으면 그 값을 반환
    if d[n] != 0:
        return d[n]

    # 1을 빼는 경우
    result = top_down(n - 1) + 1

    # 3으로 나누어 떨어지는 경우
    if n % 3 == 0:
        result = min(result, top_down(n // 3) + 1)

    # 2로 나누어 떨어지는 경우
    if n % 2 == 0:
        result = min(result, top_down(n // 2) + 1)

    # 계산 결과를 메모이제이션 배열에 저장
    d[n] = result
    return result

# 결과 출력
print(top_down(number))


d = [0] * (number+1)
# Bottom-Up
def bottom_up(number):
    for i in range(2, number + 1):
        d[i] = d[i-1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)

    return d[number]


print(bottom_up(number))
