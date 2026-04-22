"""
Purpose: Creates the graph to traverse
Nodes: Hospitals
Edges: Roads connecting hospitals
Weights: Rounded distance (miles) from one hospital to another
"""

# Adjacency list (weighted)
graph = {
    'A': [('B', 3), ('E', 9), ('D', 10)],
    'B': [('A', 3), ('C', 5)],
    'C': [('B', 5), ('J', 12), ('F', 13)],
    'D': [('A', 10), ('E', 3)],
    'E': [('D', 3), ('F', 2), ('H', 5), ('A', 9)],
    'F': [('E', 2), ('C', 13), ('K', 14)],
    'H': [('E', 5), ('I', 2), ('M', 15)],
    'I': [('H', 2)],
    'J': [('C', 12), ('L', 5), ('N', 9)],
    'K': [('L', 3), ('M', 2), ('F', 14)],
    'L': [('J', 5), ('K', 3), ('M', 4), ('N', 6)],
    'M': [('L', 4), ('K', 2), ('N', 8), ('H', 15), ('Q', 10)],
    'N': [('J', 9), ('L', 6), ('M', 8), ('O', 2), ('P', 3)],
    'O': [('N', 2), ('P', 1)],
    'P': [('O', 1), ('N', 3), ('Q', 11)],
    'Q': [('M', 10), ('P', 11)]
}
