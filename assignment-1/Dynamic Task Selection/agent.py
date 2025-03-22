import pygame
from algorithms.bfs import bfs
from algorithms.astar import astar
from algorithms.ucs import ucs
from algorithms.ida_star import ida_star

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size):
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 0, 255))  # Agent color is blue
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []
        self.path = []
        self.moving = False
        # Default algorithm: change this value to 'BFS', 'A*', 'UCS', or 'IDA*'
        self.algorithm_name = "A*"

    def move(self):
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.check_task_completion()
        else:
            self.moving = False

    def check_task_completion(self):
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)

    def find_nearest_task(self):
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            # Select pathfinding algorithm based on the agent's setting
            if self.algorithm_name == "BFS":
                path = bfs(tuple(self.position), task_position, self.get_neighbors)
            elif self.algorithm_name == "A*":
                path = astar(tuple(self.position), task_position, self.environment)
            elif self.algorithm_name == "UCS":
                path = ucs(tuple(self.position), task_position, self.environment)
            elif self.algorithm_name == "IDA*":
                path = ida_star(tuple(self.position), task_position, self.environment)
            else:
                # Fallback to A* if no valid algorithm is set
                path = astar(tuple(self.position), task_position, self.environment)

            if path and (not shortest_path or len(path) < len(shortest_path)):
                shortest_path = path
                nearest_task = task_position

        if shortest_path:
            # Exclude the current position from the path
            self.path = shortest_path[1:]
            self.moving = True

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
