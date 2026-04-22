"""
Purpose: Traverse graph using Breadth First Search
* BFS treats the weighted graph as an unweighted graph
* Searches each hospital's connection before moving on to the next one
"""

from BFS.deque import Deque
def bfs(graph, start):
    queue = Deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    order = []  # stores traversal order

    while not queue.is_empty():
        node = queue.popleft()
        order.append(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

def get_path(prev, target):
    path = []
    while target:
        path.append(target)
        target = prev[target]
    return path[::-1]