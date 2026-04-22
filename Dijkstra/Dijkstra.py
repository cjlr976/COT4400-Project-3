"""
Purpose: Diksktra's Algorithm to find the shortest path between hospitals
"""

from math import inf
from Dijkstra.minheap import MinHeap

def dijkstra(graph, start):
    heap = MinHeap()
    heap.push((0, start))

    dist = {node: inf for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    while not heap.is_empty():
        current_dist, node = heap.pop()

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heap.push((new_dist, neighbor))

    return dist, prev

#Reconstruct shortest path
def get_path(prev, target):
    path = []
    while target:
        path.append(target)
        target = prev[target]
    return path[::-1]