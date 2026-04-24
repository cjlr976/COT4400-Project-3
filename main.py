from graph import graph, print_adjacency_list
from BFS.BFS import bfs
from Prim.Prim import prim
from Dijkstra.Dijkstra import dijkstra, get_path as dij_path

def main():
    print_adjacency_list(graph)

    print("Choose an algorithm:")
    print("1. BFS traversal")
    print("2. Dijkstra shortest paths")
    print("3. Prim's algorithm")

    # Input validation
    while True:
        choice = input("\nEnter algorithm: ").strip()
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    while True:
        start = input("Enter start node: ").strip().upper()
        if start in graph:
            break
        print(f"Invalid node '{start}'. Please choose a valid node from the matrix above.\n")

    if choice == "1":
        print("\nBFS Traversal:")
        order = bfs(graph, start)
        print(order)

    if choice == "2":
        dist, prev = dijkstra(graph, start)

        print("\nDijkstra Shortest Paths from", start)
        for node in graph:
            path = dij_path(prev, node)
            print(f"{start} -> {node}: Path = {path}, Distance = {dist[node]}")

    if choice == "3":
        mst_edges, total_cost = prim(graph, start)

        print(f"\nPrim's Minimum Spanning Tree starting from {start}")
        print(f"Total Minimum Distance to Connect All: {total_cost} miles")
        print("Edges used in the MST:")

        for u, v, w in mst_edges:
            print(f"{u} -> {v} : {w} miles")

if __name__ == "__main__":
    main()