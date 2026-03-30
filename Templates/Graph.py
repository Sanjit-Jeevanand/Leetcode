from collections import deque

graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

def dfs(start, graph):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

dfs('a', graph)

print("\n\n")

def bfs(start, graph):
    q = deque([start])
    visited = {start}

    while q:
        node = q.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

bfs('a', graph)


def shortest_path(start, end, graph):
    q = deque([(start, 0)])
    visited = {start}

    while q:
        node, dist = q.popleft()
        print(node, dist)

        if node == end:
            return dist
        

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return -1

print(shortest_path('a', 'e', graph))

