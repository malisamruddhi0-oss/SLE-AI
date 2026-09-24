# 8-Puzzle Solver using BFS and DFS

## Overview

This project solves the 8-Puzzle problem using two search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The puzzle consists of 8 numbered tiles and one blank space in a 3×3 grid. The program searches for a path from the initial state to the goal state.

## Features

- BFS implementation
- DFS implementation with depth limit
- Valid move generation
- Solution path reconstruction
- Node expansion counting
- 3×3 puzzle board display

## Goal State

'''text
1 2 3
4 5 6
7 8 _

Algorithms
Breadth-First Search (BFS)
BFS explores the puzzle states level by level using a queue. For the 8-Puzzle, where every move has the same cost, BFS can find the shortest solution.

The program uses Python's deque to implement the queue.

Depth-First Search (DFS)
DFS explores one branch as deeply as possible before backtracking. It uses a stack and does not guarantee the shortest solution.

A depth limit is used to prevent excessive exploration.

Features
Solves the 8-Puzzle using BFS.
Solves the 8-Puzzle using DFS.
Generates valid tile movements.
Tracks visited states.
Reconstructs the solution path.
Counts the number of expanded nodes.
Displays the puzzle as a 3×3 board.
Uses a depth limit for DFS.
Example Input
The program uses the following starting state:

1 2 3
_ 4 6
7 5 8
Internally, this is represented as:

start_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
Output
The program displays the initial board followed by the results of BFS and DFS, including:

Number of solution moves
Number of nodes expanded
Whether DFS found a solution within the specified depth limit
Example:

BFS RESULTS:
Solution Moves: ...
Nodes Expanded: ...

DFS RESULTS:
Solution Moves: ...
Nodes Expanded: ...
Requirements
Python 3.x
No external libraries are required.
The project uses Python's built-in collections.deque.

How to Run
Open the project folder in VS Code and open the terminal.

Run:

python bfs_dfs.py
Replace bfs_dfs.py with the actual name of your Python file if it is different.

Project Structure
8-Puzzle/
│
├── bfs_dfs.py
├── README.md
└── Contribution_Log.md
BFS vs DFS
Feature	BFS	DFS
Data Structure	Queue	Stack
Search Method	Level by level	Depth first
Shortest Solution	Yes, for equal-cost moves	Not guaranteed
Memory Usage	Generally higher	Generally lower
Depth Limit	Not required	Used in this project
Learning Objectives
This project helps demonstrate:

State-space search
BFS and DFS algorithms
Queue and stack data structures
Visited-state tracking
Parent-state mapping
Path reconstruction
Basic AI search techniques
Conclusion
The project demonstrates how BFS and DFS can be applied to solve the 8-Puzzle problem. It also provides a practical comparison of how the two search strategies explore the available puzzle states.

