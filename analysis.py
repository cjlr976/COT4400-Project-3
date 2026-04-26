import time
import tracemalloc
import random

# Import your graph algorithms and baseline data
from graph import graph as baseline_graph
from BFS.BFS import bfs
from Prim.Prim import prim
from Dijkstra.Dijkstra import dijkstra

def generate_synthetic_graph(num_nodes, density):
    """
    Generates a random graph represented as an adjacency list.
    Density dictates how many extra edges are added and num_node dictates size.
    """
    # initialize empty adjacency list for all nodes
    nodes = [f"N{i}" for i in range(num_nodes)]
    graph = {node: [] for node in nodes}

    # build a basic spanning tree
    for i in range(1, num_nodes):
        u = nodes[i]
        # connect to a previously added node
        v = nodes[random.randint(0, i-1)]
        weight = random.randint(1, 20)
        
        # add undirected edge
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # add additional edges based on the desired density
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < density:
                u, v = nodes[i], nodes[j]
                
                # prevent duplicate edges
                if not any(neighbor == v for neighbor, _ in graph[u]):
                    weight = random.randint(1, 20)
                    graph[u].append((v, weight))
                    graph[v].append((u, weight))

    return graph

def measure_performance(algo_func, graph_data, start_node, algo_name, graph_name, results_dict):
    """
    Executes a given algorithm, tracks its execution time and peak memory usage, 
    and stores the results in a nested dictionary.
    """
    # Start tracking memory and time
    tracemalloc.start()
    start_time = time.perf_counter()

    # Execute the algorithm
    algo_func(graph_data, start_node)

    # Stop tracking and calculate totals
    exec_time_ms = (time.perf_counter() - start_time) * 1000
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if algo_name not in results_dict:
        results_dict[algo_name] = {}

    results_dict[algo_name][graph_name] = {
        'time': exec_time_ms,
        'memory': peak_mem / 1024 
    }

def print_terminal_reports(results, datasets):
    """
    Takes the performance metrics and prints them to the terminal
    """
    algorithms = ['BFS', 'Dijkstra', 'Prim']
    graph_names = [d[0] for d in datasets]

    # character widths to help center headers
    w_main = 61
    w_sub = 52

    print("\n" + "="*w_main)
    print("EXPERIMENTAL ANALYSIS".center(w_main))
    print("="*w_main)

    # ---  EXECUTION TIME TABLE ---
    print("\n" + "EXECUTION TIME".center(w_main))
    print(f"{'Graph Type':<15} | {'BFS (ms)':>12} | {'Dijkstra (ms)':>14} | {'Prim (ms)':>12}")
    print("-" * w_main)
    for g in graph_names:
        print(f"{g:<15} | {results['BFS'][g]['time']:>12.4f} | {results['Dijkstra'][g]['time']:>14.4f} | {results['Prim'][g]['time']:>12.4f}")

    # --- MEMORY USAGE TABLE ---
    print("\n" + "MEMORY USAGE".center(w_main))
    print(f"{'Graph Type':<15} | {'BFS (KB)':>12} | {'Dijkstra (KB)':>14} | {'Prim (KB)':>12}")
    print("-" * w_main)
    for g in graph_names:
        print(f"{g:<15} | {results['BFS'][g]['memory']:>12.2f} | {results['Dijkstra'][g]['memory']:>14.2f} | {results['Prim'][g]['memory']:>12.2f}")

    # --- GRAPH SIZE VARIATIONS ---
    print("\n" + "GRAPH SIZE VARIATIONS".center(w_sub))
    
    # Sparse
    print("\n" + "--- Sparse Graphs (Small vs Large) ---".center(w_sub))
    print(f"{'Algorithm':<10} | {'Small (16) Time':<18} | {'Large (100) Time':<18}")
    print("-" * w_sub)
    for alg in algorithms:
        print(f"{alg:<10} | {results[alg]['Small Sparse']['time']:>14.4f} ms | {results[alg]['Large Sparse']['time']:>14.4f} ms")

    # Dense
    print("\n" + "--- Dense Graphs (Small vs Large) ---".center(w_sub))
    print(f"{'Algorithm':<10} | {'Small (16) Time':<18} | {'Large (100) Time':<18}")
    print("-" * w_sub)
    for alg in algorithms:
        print(f"{alg:<10} | {results[alg]['Small Dense']['time']:>14.4f} ms | {results[alg]['Large Dense']['time']:>14.4f} ms")

    # --- SPARSE VS DENSE COMPARISONS ---
    print("\n" + "SPARSE VS DENSE COMPARISON".center(w_sub))
    
    # Large Graphs
    print("\n" + "--- Large Graphs (Sparse vs Dense) ---".center(w_sub))
    print(f"{'Algorithm':<10} | {'Sparse Time':<18} | {'Dense Time':<18}")
    print("-" * w_sub)
    for alg in algorithms:
        print(f"{alg:<10} | {results[alg]['Large Sparse']['time']:>14.4f} ms | {results[alg]['Large Dense']['time']:>14.4f} ms")

    # Small Graphs
    print("\n" + "--- Small Graphs (Sparse vs Dense) ---".center(w_sub))
    print(f"{'Algorithm':<10} | {'Sparse Time':<18} | {'Dense Time':<18}")
    print("-" * w_sub)
    for alg in algorithms:
        print(f"{alg:<10} | {results[alg]['Small Sparse']['time']:>14.4f} ms | {results[alg]['Small Dense']['time']:>14.4f} ms")

    print("\n" + "="*w_main + "\n")

def main():
    # define test scenarios
    datasets = [
        ("Current Graph", baseline_graph, "A"),                       # Baseline static graph
        ("Small Sparse", generate_synthetic_graph(200, 0.1), "N0"),    # 200 nodes, ~10% extra edges
        ("Small Dense", generate_synthetic_graph(200, 0.8), "N0"),     # 200 nodes, ~80% extra edges
        ("Large Sparse", generate_synthetic_graph(1500, 0.05), "N0"),  # 100 nodes, ~5% extra edges
        ("Large Dense", generate_synthetic_graph(1500, 0.5), "N0")     # 100 nodes, ~40% extra edges
    ]

    results_data = {}

    # Iterate through every graph dataset and test each algorithm against it
    for name, data, start in datasets:
        for algo_func, algo_name in [(bfs, "BFS"), (dijkstra, "Dijkstra"), (prim, "Prim")]:
            measure_performance(algo_func, data, start, algo_name, name, results_data)

    print_terminal_reports(results_data, datasets)

if __name__ == "__main__":
    main()