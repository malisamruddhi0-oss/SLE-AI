from collections import deque

# Goal state representation (0 represents the blank space)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_neighbors(state):
    """Generates valid next states by sliding a tile into the blank (0) space."""
    idx = state.index(0)
    r, c = idx // 3, idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            state_list = list(state)
            state_list[idx], state_list[n_idx] = state_list[n_idx], state_list[idx]
            neighbors.append(tuple(state_list))

    return neighbors

def reconstruct_path(parent_map, start_state, goal_state):
    """Traces parent references back from goal to start."""
    path = []
    curr = goal_state
    while curr != start_state:
        path.append(curr)
        curr = parent_map[curr]
    path.append(start_state)
    path.reverse()
    return path

def bfs(start_state):
    """Breadth-First Search implementation (Guarantees Shortest Path)."""
    queue = deque([start_state])
    visited = {start_state}
    parent = {}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL_STATE:
            path = reconstruct_path(parent, start_state, GOAL_STATE)
            return path, nodes_expanded

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None, nodes_expanded

def dfs(start_state, max_depth=20):
    """
    Depth-First Search implementation with a depth limit to prevent infinite loops.
    Note: DFS does NOT guarantee the shortest path.
    """
    # Stack stores tuples of: (current_state, current_depth)
    stack = [(start_state, 0)]
    visited = {start_state}
    parent = {}
    nodes_expanded = 0

    while stack:
        current, depth = stack.pop()
        nodes_expanded += 1

        if current == GOAL_STATE:
            path = reconstruct_path(parent, start_state, GOAL_STATE)
            return path, nodes_expanded

        # Explore deeper if limit isn't reached
        if depth < max_depth:
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append((neighbor, depth + 1))

    return None, nodes_expanded

def print_board(state):
    """Outputs a 9-tuple state as a 3x3 grid."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else " " for x in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)

if __name__ == "__main__":
    # Test State (8 moves away from goal)
    start_state = (1, 2, 3, 
                   0, 4, 6, 
                   7, 5, 8)

    print("Initial Board:")
    print_board(start_state)

    # Execute BFS
    bfs_path, bfs_nodes = bfs(start_state)
    print("=" * 30)
    print("BFS RESULTS:")
    print(f"Solution Moves: {len(bfs_path) - 1}")
    print(f"Nodes Expanded: {bfs_nodes}")
    print("=" * 30)

    # Execute DFS
    dfs_path, dfs_nodes = dfs(start_state, max_depth=20)
    print("\n" + "=" * 30)
    print("DFS RESULTS:")
    if dfs_path:
        print(f"Solution Moves: {len(dfs_path) - 1}")
        print(f"Nodes Expanded: {dfs_nodes}")
    else:
        print("No solution found within depth limit.")
    print("=" * 30)