# DFS, BFS
# Connected Component 정의

# The same edge is given only once
import sys
from collections import deque

def bfs(graph, start, visited):
    # Queue
    queue = deque([start])
    # 방문 처리
    visited[start] = True
    # Repeat until the queue is empty
    while queue:
        # Extract one element from the queue
        element = queue.popleft()

        for e in graph[element]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True

node, connection = map(int, sys.stdin.readline().strip().split())
# +1 to total number of nodes (to make indexing easier)
graph = [[] for _ in range(node + 1)]

# Bidirectional graph
for _ in range(connection):
    n, m = map(int, sys.stdin.readline().strip().split())
    graph[n].append(m)
    graph[m].append(n)

# Visit information
visited = [False] * (node + 1)
# Number of connected component
count = 0

for i in range(1, node + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)
