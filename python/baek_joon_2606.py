# DFS
import sys

total_node = int(sys.stdin.readline().strip())
connection = int(sys.stdin.readline().strip())

graph = [list() for _ in range(total_node+1)]
visited = [False] * (total_node+1)

input_data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(connection)]

# 양방향 연결
def Graph(graph, input_data):
    for i, j in input_data:
        graph[i].append(j)
        graph[j].append(i)

    return graph

def DFS(graph, start, visited):
    visited[start] = True
    count = 1

    for i in graph[start]:
        # False 일 때, 실행됨: None, 0, 빈 리스트 ([]), 빈 문자열 ("")
        if not visited[i]:
            count += DFS(graph, i, visited)

    return count

graph = Graph(graph, input_data)

print(DFS(graph, 1, visited) - 1)

# 다른 방법
# visited True 갯수 합 - 1
