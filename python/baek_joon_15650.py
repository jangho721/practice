# Permutation (= permutations): Order matters
# Combination (= combinations): Order does not matter
# Repetition permutation, repetition combination

# Unpacking example
# 1.
# seq = [1, 2, 3, 4]
# print(*seq)  # Output: 1 2 3 4
#
# 2.
# seq = ('apple', 'banana', 'cherry')
# print(*seq)  # Output: apple banana cherry

# Usage cases of itertools
import sys

# from itertools import combinations
#
n, m = map(int, sys.stdin.readline().strip().split())
# nlist = [num for num in range(1, n + 1)]
#
# for seq in combinations(nlist, m):
#     print(*seq)

nlist = []


def Backtraking(start):
    if len(nlist) == m:
        print(*nlist)
        return

    for i in range(start, n + 1):
        if i not in nlist:
            nlist.append(i)
            Backtraking(i + 1)
            # Last element remove
            nlist.pop()


Backtraking(1)
