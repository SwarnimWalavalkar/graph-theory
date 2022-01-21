from Graph import Graph


graph1 = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'D'],
    'C': ['F', 'A', 'B', 'D', 'F'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['A', 'C', 'E']
}


graph2 = {
    'U': ['V', 'X'],
    'V': ['Y'],
    'Y': ['X'],
    'X': ['V'],
    'W': ['Y', 'Z'],
    'Z': ['Z']
}

graph1 = Graph(graph1)
graph2 = Graph(graph2)

print(graph1)
# print(graph1.dfs())
# print("\n==========\n")
# print(graph2)
# print(graph2.dfs())
