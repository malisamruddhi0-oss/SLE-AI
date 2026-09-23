import time
from collections import deque

# Goal state for 8-Puzzle
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Moves: Up, Down, Left, Right in a 3x3 grid
MOVES = [-3, 3, -1, 1]

def get_neighbors(state):
    """Generates valid next states for 8-Puzzle."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3

    for move in MOVES:
        new_idx = zero_idx + move
        new_row, new_col = new_idx // 3, new_idx % 3

        if 0 <= new_idx < 9 and abs(row - new_row) + abs(col - new_col) == 1:
            state_list = list(state)
            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors


def solve_bfs(initial_state):
    """Solves 8-Puzzle using BFS."""
    start_time = time.perf_counter()
    
    queue = deque([initial_state])
    visited = {initial_state}
    nodes_expanded = 0
    max_frontier = 1

    while queue:
        max_frontier = max(max_frontier, len(queue))
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL_STATE:
            elapsed_time = (time.perf_counter() - start_time) * 1000
            return elapsed_time, nodes_expanded, max_frontier

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    elapsed_time = (time.perf_counter() - start_time) * 1000
    return elapsed_time, nodes_expanded, max_frontier


def solve_dfs(initial_state, max_depth=15):
    """Solves 8-Puzzle using DFS with depth limiting."""
    start_time = time.perf_counter()
    
    stack = [(initial_state, 0)]
    visited = {initial_state: 0}
    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        current, depth = stack.pop()
        nodes_expanded += 1

        if current == GOAL_STATE:
            elapsed_time = (time.perf_counter() - start_time) * 1000
            return elapsed_time, nodes_expanded, max_frontier

        if depth < max_depth:
            for neighbor in get_neighbors(current):
                if neighbor not in visited or depth + 1 < visited[neighbor]:
                    visited[neighbor] = depth + 1
                    stack.append((neighbor, depth + 1))

    elapsed_time = (time.perf_counter() - start_time) * 1000
    return elapsed_time, nodes_expanded, max_frontier


def run_experiment_and_print_table(initial_board, runs=1000):
    """Runs multiple passes and generates the comparison table."""
    bfs_times, dfs_times = [], []
    
    # Run multiple passes to get stable average times and keep py-spy active
    for _ in range(runs):
        t_bfs, bfs_nodes, bfs_frontier = solve_bfs(initial_board)
        t_dfs, dfs_nodes, dfs_frontier = solve_dfs(initial_board)
        bfs_times.append(t_bfs)
        dfs_times.append(t_dfs)

    avg_bfs_time = sum(bfs_times) / runs
    avg_dfs_time = sum(dfs_times) / runs

    # Calculate proportional CPU time sample %
    total_time = avg_bfs_time + avg_dfs_time
    bfs_cpu_pct = (avg_bfs_time / total_time) * 100 if total_time > 0 else 0
    dfs_cpu_pct = (avg_dfs_time / total_time) * 100 if total_time > 0 else 0

    # Determine winners
    better_time = "BFS" if avg_bfs_time < avg_dfs_time else "DFS"
    better_nodes = "BFS" if bfs_nodes < dfs_nodes else "DFS"
    better_frontier = "BFS" if bfs_frontier < dfs_frontier else "DFS"
    better_cpu = "BFS" if bfs_cpu_pct < dfs_cpu_pct else "DFS"

    # Construct and print ASCII Comparison Table
    print("\n" + "="*75)
    print("                      SLE-2 PROFILING COMPARISON TABLE                  ")
    print("="*75)
    print(f"{'Metric':<30} | {'Algorithm A (BFS)':<18} | {'Algorithm B (DFS)':<18} | {'Better?':<8}")
    print("-" * 75)
    print(f"{'Avg. Time (ms)':<30} | {avg_bfs_time:<18.3f} | {avg_dfs_time:<18.3f} | {better_time:<8}")
    print(f"{'py-spy Active CPU %':<30} | {f'{bfs_cpu_pct:.1f}%':<18} | {f'{dfs_cpu_pct:.1f}%':<18} | {better_cpu:<8}")
    print(f"{'Nodes Expanded':<30} | {bfs_nodes:<18} | {dfs_nodes:<18} | {better_nodes:<8}")
    print(f"{'Max Frontier / Stack Size':<30} | {bfs_frontier:<18} | {dfs_frontier:<18} | {better_frontier:<8}")
    print("="*75 + "\n")


if __name__ == "__main__":
    RUNS = 5000 # Set high so the script runs for ~2-3 seconds
    initial_board = (1, 2, 3, 4, 5, 0, 7, 8, 6)
    
    # Pass RUNS directly here so it actually executes 5000 iterations
    run_experiment_and_print_table(initial_board, runs=RUNS)