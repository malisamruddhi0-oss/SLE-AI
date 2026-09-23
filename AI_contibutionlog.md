# CONTRIBUTIONS.md

## Step-by-Step Joint Contribution Log

### Step 1: Benchmarking & Profiling Setup (`py-spy`)
* **What You Did:** 
  * Provided initial profiling code patterns from your `bfs_dfs` graph project.
  * Specified that you wanted to run `py-spy` profiling on an 8-Puzzle comparison.
* **What AI Did:** 
  * Created `puzzle_profiling.py` using multi-iteration test loops (`REPETITIONS`) across variable puzzle difficulties to give `py-spy` a sufficient sampling window.
  * Diagnosed profiler output issues where `importlib` dominated sampling frames, guiding configuration fixes.
Step 2: Core Algorithm Development (BFS & DFS)What You Did:Requested clean implementations of Breadth-First Search (BFS) and Depth-First Search (DFS) for the 8-Puzzle state space.Specified the requirement to view step-by-step board states and total node expansion counts.What AI Did:Implemented BFS using collections.deque and bounded DFS using a LIFO stack list.Encoded states as flat hashable tuples (1, 2, 3, 4, 5, 6, 7, 8, 0) for $O(1)$ visited state verification.Built depth-limiting parameters inside DFS (max_depth=20) to prevent infinite recursion on graph cycles.Authored reconstruct_path() and print_board() utilities for visual board rendering.

Step 3: Documentation & Project FormattingWhat You Did:Requested project documentation files including README.md and CONTRIBUTIONS.md.Evaluated initial documentation drafts and redirected structural formatting to emphasize explicit, step-by-step task distributions for human vs. AI roles.What AI Did:Drafted the full project README.md complete with complexity comparisons, technical feature breakdowns, and terminal usage instructions.Formatted this CONTRIBUTIONS.md file tracking the exact chronological joint workflow.

Step 4: Verification & Local ExecutionWhat You Did:Executed puzzle_solver.py locally to verify solution paths and node expansion counts.Validated that BFS returned optimal move paths while DFS executed deeper state explorations.What AI Did:Verified logic correctness and ensured code structure followed Python standards.
  -