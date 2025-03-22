# algorithms/ucs.py
import heapq

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

def ucs(start, goal, environment):
    """Uniform Cost Search (Dijkstra's algorithm) to find the shortest path from start to goal."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_set:
        current_cost, current = heapq.heappop(open_set)
        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in get_neighbors(current, environment):
            new_cost = cost_so_far[current] + 1  # Cost for each move is 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(open_set, (new_cost, neighbor))
    return None  # No path found
