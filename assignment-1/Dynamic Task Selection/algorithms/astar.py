# algorithms/astar.py
import heapq

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

def astar(start, goal, environment):
    """A* Search algorithm to find the shortest path from start to goal."""
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        f, current_g, current = heapq.heappop(open_set)
        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current, environment):
            tentative_g = current_g + 1  # Cost from current to neighbor is 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    return None  # No path found
