from collections import deque

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    visited = [[False]*cols for _ in range(rows)]
    parent = [[None]*cols for _ in range(rows)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            # Reconstruct path
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[x][y]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
    
    return None  # No path found


# Example Maze (0=open, 1=blocked)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 4)

path = bfs_maze(maze, start, goal)
if path:
    print("Shortest Path:", path)
else:
    print("No path found.")
