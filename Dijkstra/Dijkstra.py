"""
Purpose: Traverse graph using Diksktra's Algorithm to find the shortest path between hospitals
* Use MinHeap to keep track of visited nodes
* Use priority queue to contain all vertices in Graph

Nodes: Hospitals
Edges: Roads connecting hospitals
Type: Undirected, weighted
Weights: Rounded distance (miles) from one hospital to another
"""

from math import inf
import heapq

def dijkstra(graph, start):
    # Priority queue: (distance, node)
    pq = []
    heapq.heappush(pq, (0, start))

    dist = {node: inf for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip outdated entries
        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            
            #Relaxation
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, prev

# Reconstruct shortest path
def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]