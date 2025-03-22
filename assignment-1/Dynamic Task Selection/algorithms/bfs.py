from collections import deque

def bfs(start, goal, get_neighbors):
    """Find the shortest path using BFS."""
    queue = deque([[start]])
    visited = set()
    visited.add(start)

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        for neighbor in get_neighbors(x, y):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)
    return None  # No path found