# Lab 3(c): Grid-Based Robot Navigation with Multiple Search Algorithms

## Introduction

This repository is a fork of the original Lab 3: Grid-Based Robot Navigation Simulation. I forked this repository to complete my lab task, focusing solely on the third version (Lab 3(c)). My goal was to experiment with different search algorithms for pathfinding in a grid-based environment.

The agent (robot) navigates a grid, selecting the nearest task while avoiding barriers. I have implemented and tested the following search algorithms:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A* Search (A*)**
- **Iterative Deepening A* (IDA*)**
- **Uniform Cost Search (UCS)**

## Setup

### Requirements

- Python 3.6 or later
- Pygame library

### Installation

Clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/lab3c-search-algorithms.git
```

Navigate to the repository:

```sh
cd lab3c-search-algorithms
```

Install Pygame if it's not already installed:

```sh
pip install pygame
```

## Running the Simulation

Run the simulation using:

```sh
python run.py
```

A Pygame window will open, displaying the grid, agent, tasks, and barriers. The agent dynamically selects the nearest task and navigates using the chosen search algorithm.

## Search Algorithms Implemented

- **BFS (Breadth-First Search):** Explores all nodes at the present depth level before moving to the next level.
- **DFS (Depth-First Search):** Explores as far as possible along each branch before backtracking.
- **A* Search (A*):** Uses a heuristic function to optimize pathfinding by estimating the cost to reach the goal.
- **UCS (Uniform Cost Search):** Expands the least-cost node, ensuring optimal paths in weighted graphs.
- **IDA* (Iterative Deepening A*):** Combines depth-first search with A\* heuristics for memory-efficient pathfinding.

## Code Structure

- `agent.py`: Defines the Agent class, including movement and pathfinding logic.
- `environment.py`: Manages the grid setup, task placement, barriers, and utility functions.
- `run.py`: The main script initializing the simulation and handling user interactions.

## Features

- **Nearest-task selection:** The agent dynamically selects the closest task for efficiency.
- **Multiple search algorithms:** Easily switch between different pathfinding strategies.
- **Real-time visualization:** Observe the agent’s decision-making process live.

## Additional Notes

- You can modify parameters (e.g., `num_tasks`, `num_barriers`) in `run.py` to test different configurations.
- Future enhancements could include additional heuristics, multi-agent navigation, or dynamic obstacle avoidance.

---

This project helped me explore various search algorithms for pathfinding and analyze their efficiency in a grid-based navigation system.
