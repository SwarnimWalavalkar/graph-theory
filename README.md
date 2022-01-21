# Graph Theory Experiments

Cuz graphs are fun...

Constructing a Graph with `Graph.py`

```python
graph = Graph({
    'U': ['V', 'X'],
    'V': ['Y'],
    'Y': ['X'],
    'X': ['V'],
    'W': ['Y', 'Z'],
    'Z': ['Z']
})
```

Or:

```python
graph = Graph()

graph.addNode('U')
graph.addNode('V')
graph.addNode('Y')
graph.addNode('X')
graph.addNode('W')
graph.addNode('Z')

graph.addEdge('U', 'V')
graph.addEdge('U', 'X')
graph.addEdge('V', 'Y')
graph.addEdge('Y', 'X')
graph.addEdge('X', 'V')
graph.addEdge('W', 'Y')
graph.addEdge('W', 'Z')
graph.addEdge('Z', 'Z')
```
