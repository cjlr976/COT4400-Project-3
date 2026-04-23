"""
Purpose: Traverse graph using Breadth First Search
* BFS treats the weighted graph as an unweighted graph
* Searches each hospital's connection before moving on to the next one
"""
from collections import deque

def bfs(graph, start):
    queue = deque([start]) # initialize with start node
    visited = set([start])
    order = []  # stores traversal order

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order