# 8-Puzzle Solver using BFS and DFS

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student Name:** SAMRUDDHI PRAKASH MALI  
**PRN:** 25UAM097  
**Division:** B  
**Date:** 03/10/2026[cite: 1]  

---

## 1. System Overview & Project Description

The **8-Puzzle Solver** is an AI search system designed to find a sequence of valid moves from an initial $3 \times 3$ puzzle configuration to a specified goal configuration[cite: 1]. The system represents state nodes and generates successor states by sliding tiles into the blank space[cite: 1]. It utilizes two foundational uninformed search algorithms:

* **Breadth-First Search (BFS):** Explores the state space level-by-level using a FIFO queue to guarantee the shortest path solution[cite: 1].
* **Depth-First Search (DFS):** Explores deeply along each branch using a LIFO stack to minimize memory usage in shallow branches[cite: 1].

---

## 2. Software Architecture (C4 Model)

The architecture is structured according to the C4 model guidelines[cite: 1]:

### Level 1: Context Diagram
* **User Interaction:** The user inputs the starting $3 \times 3$ grid, selects the preferred algorithm (BFS or DFS), and receives the completed step-by-step solution path[cite: 1].

### Level 2: Container Diagram
* **Input Module:** Captures the initial state, target goal state, and algorithm selection[cite: 1].
* **Search Engine:** Drives the BFS or DFS search process across state boundaries[cite: 1].
* **State Manager:** Calculates valid moves and maintains a record of visited states to eliminate duplicate state exploration[cite: 1].
* **Goal & Path Module:** Evaluates goal conditions and reconstructs full paths upon search completion[cite: 1].
* **Output Module:** Formats and prints the final state traversal and solution execution sequence[cite: 1].

### Level 3: Component Diagram (Search Engine Breakdown)
* **Frontier (Queue/Stack):** Manages pending states (FIFO queue for BFS, LIFO stack for DFS)[cite: 1].
* **Visited Set:** Hashes visited configurations to avoid cyclical search loops[cite: 1].
* **Goal Test:** Evaluates state equivalence against the target matrix[cite: 1].
* **Path Reconstructor:** Re-traces back-pointers from goal node to start node to return ordered move sequences[cite: 1].

### Level 4: Code Design
* `class Node`: Tracks current grid state, parent pointer, action taken, and path cost[cite: 1].
* `class Puzzle`: Encapsulates grid dimensions ($3 \times 3$) and move validities[cite: 1].
* `def bfs()` / `def dfs()`: Search implementation entry points[cite: 1].
* `def is_goal()`: Evaluates matching criteria[cite: 1].
* `def get_neighbors()`: Identifies valid sliding moves (up, down, left, right)[cite: 1].
* `def reconstruct_path()`: Generates chronological sequence of solutions[cite: 1].

---

## 3. Getting Started & Execution

1. Clone or download the source files.
2. Ensure Python 3.x is installed on your environment.
3. Run the driver code:
   ```bash
   python main.py
