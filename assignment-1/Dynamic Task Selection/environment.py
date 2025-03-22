# environment.py
import random

class Environment:
    def __init__(self, width, height, grid_size, num_tasks, num_barriers):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.columns = width // grid_size
        self.rows = height // grid_size
        self.task_locations = self.generate_tasks(num_tasks)
        self.barrier_locations = self.generate_random_locations(num_barriers, exclude=set(self.task_locations.keys()))

    def generate_tasks(self, count):
        """Generate task locations with unique task numbers."""
        tasks = {}
        for task_number in range(1, count + 1):
            while True:
                location = (random.randint(0, self.columns - 1), random.randint(0, self.rows - 1))
                if location not in tasks:
                    tasks[location] = task_number
                    break
        return tasks

    def generate_random_locations(self, count, exclude=set()):
        """Generate unique random locations that are not in the exclude set."""
        locations = set()
        while len(locations) < count:
            location = (random.randint(0, self.columns - 1), random.randint(0, self.rows - 1))
            if location not in exclude:
                locations.add(location)
        return locations

    def is_within_bounds(self, x, y):
        """Check if (x, y) is within the grid boundaries."""
        return 0 <= x < self.columns and 0 <= y < self.rows

    def is_barrier(self, x, y):
        """Check if (x, y) is a barrier."""
        return (x, y) in self.barrier_locations
