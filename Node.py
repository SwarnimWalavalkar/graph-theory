class Node:
    def __init__(self, nodeLabel):
        self.label = nodeLabel
        self.adjacent = {}

    def __str__(self):
        return str(f"'{self.label}' adjacent: {str([ n.label for n in self.adjacent])}")

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getEdges(self):
        return self.adjacent.keys()

    def getLabel(self):
        return self.label

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
