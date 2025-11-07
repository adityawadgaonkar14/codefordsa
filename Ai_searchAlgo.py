from collections import deque

# Function to perform BFS in a maze
def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])  # Queue for BFS
    visited = set()
    parent = {}  # To track the path

    # Movement directions (up, down, left, right)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited.add(start)

    while queue:
        current = queue.popleft()

        if current == goal:
            # Trace back the path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path  # Return shortest path

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            if (0 <= new_x < rows and 0 <= new_y < cols and 
                maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                parent[(new_x, new_y)] = current

    return None  # If no path found


# -------- MAIN PROGRAM --------
rows = int(input("Enter number of rows in maze: "))
cols = int(input("Enter number of columns in maze: "))

maze = []
print("Enter the maze row by row (0 for open path, 1 for wall):")
for i in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

path = bfs(maze, start, goal)

if path:
    print("\nPath found:", path)
    # Visualization
    print("\nMaze visualization (S=start, G=goal, *=path):")
    for i in range(rows):
        for j in range(cols):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif (i, j) in path:
                print("*", end=" ")
            elif maze[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No path found!")
