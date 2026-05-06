from collections import deque

def bfs_shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return "Invalid users"

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return "No path found"


def dfs(graph, start, depth, visited=None):
    if start not in graph:
        return "Invalid user"

    if visited is None:
        visited = set()

    if depth < 0:
        return visited

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, depth - 1, visited)

    return sorted(visited)