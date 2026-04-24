"""
Purpose: Traverse graph using Prim's Algorithm to find the Minimum Spanning Tree
* Uses a MinHeap to continually pick the shortest edge connecting the tree to an unvisited node
* Avoids cycles by checking a 'visited' set
"""

import heapq

def prim(graph, start):
    priority_queue = []
    visited = set()
    mst_edges = []
    total_weight = 0

    # Initialize by adding the starting node and its available edges
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)

        # Only process unvisited nodes to prevent cycles
        if v not in visited:
            visited.add(v)
            mst_edges.append((u,v, weight))
            total_weight += weight

            # Evaluate edges branching out from the newly added node
            for neighbor, weight in graph[v]:
                # push more neighbors
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, v, neighbor))

    return mst_edges, total_weight