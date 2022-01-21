from Node import Node
from queue import Queue


class Graph:
    def __init__(self, graphStrct=None):
        self.nodes = {}
        self.totalNodes = 0

        if graphStrct is not None:
            for node in graphStrct:
                if node not in self.nodes:
                    self.addNode(node)
                for edge in graphStrct[node]:
                    self.addEdge(node, edge)

    def __iter__(self):
        return iter(self.nodes.values())

    def __str__(self):
        output = ""
        for node in self:
            output = output + str(node) + "\n"
        return output

    def addNode(self, node):
        self.totalNodes += 1
        newNode = Node(node)
        self.nodes[node] = newNode
        return newNode

    def getNode(self, node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            return None

    def addEdge(self, node1, node2, cost=0):
        if node1 not in self.nodes:
            self.addNode(node1)
        if node2 not in self.nodes:
            self.addNode(node2)

        self.nodes[node1].addNeighbor(self.nodes[node2], cost)
        self.nodes[node2].addNeighbor(self.nodes[node1], cost)

    def getNodes(self):
        return self.nodes.keys()

    def dfs(self, node=None, visited=None):
        if visited is None:
            visited = []
        if node is not None:
            if node.getLabel() not in visited:
                visited.append(node.getLabel())
                for neighbor in node.getEdges():
                    self.dfs(neighbor, visited)

        for node in self:
            if node.getLabel() not in visited:
                self.dfs(node, visited)
        return visited

    def bfs(self, start):
        visited = {}
        level = {}
        parent = {}
        path = []
        queue = Queue()

        for node in self:
            visited[node.getLabel()] = False
            parent[node.getLabel()] = None
            level[node.getLabel()] = -1

        visited[start.getLabel()] = True
        level[start.getLabel()] = 0
        queue.put(start)

        while not queue.empty():
            node = queue.get()
            path.append(node.getLabel())
            for neighbor in node.getEdges():
                if not visited[neighbor.getLabel()]:
                    visited[neighbor.getLabel()] = True
                    parent[neighbor.getLabel()] = node.getLabel()
                    level[neighbor.getLabel()] = level[node.getLabel()] + 1
                    queue.put(neighbor)

        return path, visited, level, parent
