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


path1, visited1, level1, parent1 = graph1.bfs(graph1.getNode("A"))
print(graph1, end="\n")
print(
    f"path: {path1}, \nvisited: {visited1}, \nlevel: {level1}, \nparent: {parent1}\n")

path2, visited2, level2, parent2 = graph2.bfs(graph2.getNode("U"))
print(graph2, end="\n")
print(f"path: {path2}, \nvisited: {visited2}, \nlevel: {level2}, \nparent: {parent2}\n\n")

nodeToFind1 = graph1.getNode("D")

shortestPath1 = []

while nodeToFind1 is not None:
    shortestPath1.append(nodeToFind1.getLabel())
    nodeToFind1 = parent1[nodeToFind1.getLabel()]
shortestPath1.reverse()

print(f"Shortest path from A to D is: {shortestPath1}")
