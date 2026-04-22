from graph import graph
from BFS.BFS import bfs
from Dijkstra.Dijkstra import dijkstra, get_path as dij_path

def main():
    print("Choose algorithm:")
    print("1 BFS traversal")
    print("2 Dijkstra shortest paths")

    choice = input("Enter algorithm: ").strip()
    start = input("Enter start node: ").strip().upper()

    if choice == "1":
        print("\nBFS Traversal:")
        order = bfs(graph, start)
        print(order)

    elif choice == "2":
        dist, prev = dijkstra(graph, start)

        print("\nDijkstra Shortest Paths from", start)
        for node in graph:
            path = dij_path(prev, node)
            print(f"{start} -> {node}: Path = {path}, Distance = {dist[node]}")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()