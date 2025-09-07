# 문제 이해가 늦었음...
import sys

string = sys.stdin.readline().rstrip()
result = ["" for _ in range(len(string))]

def zoac(ind, string): # ind : 시작 index

    if not string:
        return

    temp = min(string)
    idx = string.index(temp)
    result[ind+idx] = temp

    print("".join(result))

    # 재귀
    zoac(ind+idx+1, string[idx+1:])
    zoac(ind, string[:idx])

zoac(0, string)
