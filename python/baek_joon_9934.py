import sys

# Complete Binary Tree

# traversal
# preorder: Root, L, R
# inorder: L, Root, R (This case)
# postorder: L, R, Root
def traversal(start, end, level):
    if start == end:
        results[level].append(inorder_tree[start])
        return
    center = (start + end) // 2
    results[level].append(inorder_tree[center])
    traversal(start, center - 1, level + 1)
    traversal(center + 1, end, level + 1)


level = int(sys.stdin.readline().strip())
inorder_tree = list(map(int, sys.stdin.readline().strip().split()))
length = len(inorder_tree)

results = [[] for _ in range(level)]
traversal(0, length - 1, 0)

for line in results:
    print(*line)
