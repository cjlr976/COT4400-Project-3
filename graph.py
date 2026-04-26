"""
Purpose: Creates the graph to traverse
Nodes: Hospitals
Edges: Roads connecting hospitals
Weights: Rounded distance (miles) from one hospital to another
"""

# Adjacency list (weighted)
graph = {
    'A': [('B', 3), ('D', 10), ('E', 9)],
    'B': [('A', 3), ('C', 5)],
    'C': [('B', 5), ('F', 13), ('J', 12)],
    'D': [('A', 10), ('E', 3), ('G', 5)],
    'E': [('A', 9), ('D', 3), ('F', 2), ('H', 5)],
    'F': [('C', 13), ('E', 2),  ('K', 14)],
    'G': [('D', 5), ('H', 3), ('I', 2)],
    'H': [('E', 5), ('G', 3), ('I', 2), ('M', 15)],
    'I': [('G', 2), ('H', 2)],
    'J': [('C', 12), ('L', 5), ('N', 9)],
    'K': [('F', 14), ('L', 3), ('M', 2)],
    'L': [('J', 5), ('K', 3), ('M', 4), ('N', 6)],
    'M': [('H', 15), ('K', 2), ('L', 4), ('N', 8), ('Q', 10)],
    'N': [('J', 9), ('L', 6), ('M', 8), ('O', 2), ('P', 3)],
    'O': [('N', 2), ('P', 1)],
    'P': [('N', 3), ('O', 1), ('Q', 11)],
    'Q': [('M', 10), ('P', 11)]
}

def print_adjacency_list(graph):
    print("\n--- Hospital Graph Adjacency List ---")
    for node, edges in graph.items():
        # Formats edges as: A -> B(3), E(9), D(10)
        edge_strings = [f"{neighbor}({weight})" for neighbor, weight in edges]
        print(f"{node} -> {', '.join(edge_strings)}")
    print("-------------------------------------\n")
