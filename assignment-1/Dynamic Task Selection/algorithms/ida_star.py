# algorithms/ida_star.py
def heuristic(a, b):
    """Compute the Manhattan distance heuristic between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, environment):
    """Return walkable neighbors for the node within the environment."""
    neighbors = []
    x, y = node
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if environment.is_within_bounds(nx, ny) and not environment.is_barrier(nx, ny):
            neighbors.append((nx, ny))
    return neighbors

def ida_star(start, goal, environment):
    """
    Iterative Deepening A* (IDA*) search algorithm.
    
    Returns the path from start to goal if found, else None.
    """
    threshold = heuristic(start, goal)
    path = [start]
    while True:
        temp = _ida_search(path, 0, threshold, goal, environment)
        if isinstance(temp, list):  # Found path
            return temp
        if temp == float('inf'):
            return None  # No path exists
        threshold = temp

def _ida_search(path, g, threshold, goal, environment):
    node = path[-1]
    f = g + heuristic(node, goal)
    if f > threshold:
        return f
    if node == goal:
        return list(path)
    minimum = float('inf')
    for neighbor in get_neighbors(node, environment):
        if neighbor in path:  # Avoid cycles
            continue
        path.append(neighbor)
        temp = _ida_search(path, g + 1, threshold, goal, environment)
        if isinstance(temp, list):  # Found path
            return temp
        if temp < minimum:
            minimum = temp
        path.pop()
    return minimum
