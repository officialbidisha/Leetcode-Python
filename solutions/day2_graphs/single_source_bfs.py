from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    steps = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            print(f"level {steps}: popped {node}")

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        steps += 1
    return steps


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'F'],
        'E': ['C', 'F'],
        'F': ['D', 'E'],
    }
    print(bfs(graph, 'A'))